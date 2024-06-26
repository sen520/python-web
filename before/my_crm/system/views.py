from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_GET
from django.http.response import JsonResponse
from .models import *
from hashlib import md5
from django.core.exceptions import ObjectDoesNotExist
import json
from my_crm.common import ParamException, is_empty
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from system.models import *


# Create your views here.


@require_POST
def login(request):
    # 获取参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 非空验证
    is_empty(username, message='请输入账号')
    is_empty(password, message='请输入密码！')
    # 如果用户已登录，不需要登录
    user_str = request.session.get('login_user')
    if user_str:
        raise ParamException(code=2, message='用户已登录！')

    # 先将password进行md5加密
    md = md5(password.encode(encoding='utf-8'))
    password_md5 = md.hexdigest()
    try:
        user = User.objects.values('id', 'userName', 'trueName', 'phone',
                                   'email').get(userName=username, password=password_md5)
        # 保持登录状态
        request.session['login_user'] = json.dumps(user)

        # 获取用户可操作的资源列表保存到session
        # 登录登录用户的id获取用户的角色，再根据角色获取操作的资源列表
        user_role_ids = UserRole.objects.values_list('role__id', flat=True) \
            .filter(user__id=user.get('id')).all()
        print(user_role_ids)
        user_permissions = Permission.objects.values_list('aclValue', flat=True) \
            .filter(role__id__in=list(user_role_ids)).all()
        request.session['login_user_permissions'] = list(user_permissions)

        return JsonResponse({'code': 1, 'message': '登录成功！'})
    except ObjectDoesNotExist as e:
        raise ParamException(message='用户或密码失败！')
        # return JsonResponse({'code': 0, 'message': '用户或密码失败！'})


@require_POST
def update_password(request):
    # a) 是否用户处于登录状态
    user_str = request.session.get('login_user')
    is_empty(user_str, message='请登录')

    # b) 非空校验，新密码和确认密码也要校验
    old_password = request.POST.get('old_password')
    is_empty(old_password, message='请输入原密码')
    new_password = request.POST.get('new_password')
    is_empty(new_password, message='请输入新密码')
    confirm_new_password = request.POST.get('confirm_new_password')
    is_empty(confirm_new_password, message='请输入确认新密码')
    if new_password != confirm_new_password:
        raise ParamException.create_error('两次密码输入不相等')

    # c) 原密码是否正确，就是将原密码(加密)  和数据库中的密码进行对比
    user = json.loads(user_str, encoding='utf-8')
    user_obj = User.objects.get(pk=user.get('id'))
    password = user_obj.password
    md = md5(old_password.encode(encoding='utf-8'))
    old_password = md.hexdigest()
    if password != old_password:
        return JsonResponse({'code': 0, 'message': '原密码输入不正确，请重新输入'})
    # d) 修改密码
    user_obj.password = md5(new_password.encode(encoding='utf-8')).hexdigest()
    user_obj.save()
    # e) 返回结果
    return JsonResponse({'code': 1, 'message': '修改成功！'})


def logout(request):
    request.session.flush()
    return redirect('index:index')


# 查询客户经理
def find_customer_manager(request):
    managers = User.objects.values("id", 'userName', 'trueName') \
        .filter(roles__roleName='客户经理') \
        .order_by('-id').all()
    managers = list(managers)
    return JsonResponse(managers, safe=False)


# 资源列表
def module_index(request):
    return render(request, 'module_index.html')


# 分页查询
@require_GET
def select_module(request):
    # 分页参数
    page = request.GET.get('page')
    page_size = request.GET.get('rows')
    # 分页数据集合
    queryset = Module.objects.values('id', 'moduleName', 'moduleStyle',
                                     'url', 'parent', 'parentOptValue',
                                     'grade', 'optValue', 'orders', 'updateDate').all()
    # 分页对象
    p = Paginator(queryset, page_size)
    # 分页结果
    total = p.count
    rows = list(p.page(page).object_list)
    # 返回
    return JsonResponse({'rows': rows, 'total': total})


# 获取层级下的模块
@require_GET
def find_by_grade(request):
    grade = request.GET.get('grade')
    modules = Module.objects.values('id', 'moduleName').filter(grade=grade).all()
    return JsonResponse(list(modules), safe=False)


# 添加模块
@require_POST
@csrf_exempt
def add_module(request):
    # 获取参数
    module = request.POST.dict()
    del module['id']
    # 参数非空校验
    # TODO
    # 操作权限值唯一校验
    opt_value = module.get('optValue')
    try:
        Module.objects.get(optValue=opt_value)
        return JsonResponse({'code': 0, 'message': '该操作权限值已存在，请确认后重试！'})
    except ObjectDoesNotExist as e:
        pass

    # 构建tree_path
    grade = module.get('grade')
    is_empty(grade, message='请选择层级！')
    parent_id = module.pop('parentId')
    if int(grade) > 0:
        is_empty(parent_id, message='请选择上级菜单！')
        tree_path = ''
        # 先查询父级
        parent = Module.objects.get(pk=parent_id)
        parent_tree_path = parent.treePath
        if not parent_tree_path:
            tree_path = ',%s,' % parent_id
        else:
            tree_path = parent_tree_path + parent_id + ','
        module['treePath'] = tree_path
        module['parent'] = parent
    module['isValid'] = 1
    module['createDate'] = timezone.now()
    module['updateDate'] = timezone.now()
    # 保存
    obj = Module.objects.create(**module)

    # 把此资源绑定到系统管理员中
    role = Role.objects.get(pk=1)
    Permission.objects.create(module=obj, role=role, aclValue=opt_value,
                              isValid=1, updateDate=timezone.now(), createDate=timezone.now())
    # 返回
    return JsonResponse({'code': 1, 'message': '添加成功！'})


# 修改资源
@require_POST
@csrf_exempt
def update_module(request):
    # 获取参数
    module = request.POST.dict()
    pk = module.pop('id')
    # 参数非空校验
    # TODO
    # 操作权限值唯一校验
    opt_value = module.get('optValue')
    # 先获取数据库中对象
    module_from_db = Module.objects.get(pk=pk)
    if module_from_db.optValue != opt_value:
        try:
            Module.objects.get(optValue=opt_value)
            return JsonResponse({'code': 0, 'message': '该操作权限值已存在，请确认后重试！'})
        except ObjectDoesNotExist as e:
            pass

    # 构建tree_path
    grade = module.get('grade')
    if int(grade) > 0:
        parent_id = module.pop('parentId')
        if int(parent_id) != module_from_db.parent_id:
            # 构建
            # 先查询父级
            parent = Module.objects.get(pk=parent_id)
            parent_tree_path = parent.treePath
            if not parent_tree_path:
                tree_path = ',%s,' % parent_id
            else:
                tree_path = parent_tree_path + parent_id + ','
            module['treePath'] = tree_path
            module['parent'] = parent

    module['updateDate'] = timezone.now()
    Module.objects.filter(pk=pk).update(**module)
    return JsonResponse({'code': 1, 'message': '修改成功！'})


# 删除
@require_POST
@csrf_exempt
def delete_module(request):
    # 获取主键ids
    ids = request.POST.get('ids')
    # 更新 isValid=0
    id_arr = ids.split(',')
    # 如果此资源已被角色关联，那么不要删除
    for pk in id_arr:
        amount = Permission.objects.filter(module__id=pk).count()
        if amount == 0:
            Module.objects.filter(pk=pk).update(isValid=0, updateDate=timezone.now())
    # Module.objects.filter(pk__in=ids.split(',')).update(isValid=0, updateDate=timezone.now())
    # 返回
    return JsonResponse({'code': 1, 'message': '删除成功！'})


# 跳转到模板
def role_index(request):
    return render(request, 'role_index.html')


# 分页查询数据
@require_GET
def select_role(request):
    # 查询的命令
    select = {'createDate': 'SELECT DATE_FORMAT(create_date, "%%Y-%%m-%%d %%H:%%i:%%s")',
              'updateDate': 'SELECT DATE_FORMAT(update_date, "%%Y-%%m-%%d %%H:%%i:%%s")'}
    queryset = Role.objects.extra(select=select) \
        .values('id', 'roleName', 'roleRemark', 'createDate', 'updateDate').all()
    # 获取分页的参数 page page_size
    page = request.GET.get('page', 1)
    page_size = request.GET.get('rows', 10)
    # 构建分页对象
    p = Paginator(queryset, page_size)  # 传入结果集以及每页多少条
    # 分页查询结果集
    rows = p.page(page).object_list
    # 返回数据
    return JsonResponse({'rows': list(rows), 'total': p.count})


# 添加数据
@require_POST
@csrf_exempt
def add_role(request):
    # 获取参数
    role = request.POST.dict()
    # 基本参数校验
    # TODO

    # 唯一性校验
    role_name = role.get('roleName')
    is_empty(role_name, message='请填写角色名称!')
    try:
        Role.objects.get(roleName=role_name)
        return JsonResponse({'code': 0, 'message': '该角色已存在，请确认后重试！'})
    except ObjectDoesNotExist as e:
        pass
    # 添加默认字段值
    role['isValid'] = 1
    role['createDate'] = timezone.now()
    role['updateDate'] = timezone.now()
    # 添加数据
    Role.objects.create(**role)
    return JsonResponse({'code': 1, 'message': '添加成功！'})


# 修改角色
@require_POST
@csrf_exempt
def update_role(request):
    role = request.POST.dict()
    pk = role.pop('id')
    # 基本参数校验
    # 唯一性校验
    role_from_db = Role.objects.get(pk=pk)
    role_name = role.get('roleName')
    if role_name != role_from_db.roleName:
        try:
            Role.objects.get(roleName=role_name)
            return JsonResponse({'code': 0, 'message': '该角色已存在，请确认后重试！'})
        except ObjectDoesNotExist as e:
            pass
    role['updateDate'] = timezone.now()
    Role.objects.filter(pk=pk).update(**role)
    return JsonResponse({'code': 1, 'message': '修改成功！'})


# 删除角色
@require_POST
@csrf_exempt
def delete_role(request):
    ids = request.POST.get('ids')
    Role.objects.filter(pk__in=ids.split(',')).update(isValid=0, updateDate=timezone.now())
    # TODO
    # 删除角色绑定的资源
    return JsonResponse({'code': 1, 'message': '删除成功！'})


def test_ztree(request):
    return render(request, 'test_ztree.html')


# 给角色赋予操作模块的权限页面
def relate_modules_index(request, role_id):
    # { id:1, pId:0, name:"随意勾选 1", open:true}
    all_modules = Module.objects.values('id', 'moduleName', 'parent').all()
    # 获取角色的权限
    role_has_module_ids = Permission.objects.values_list('module__id', flat=True).filter(role__id=role_id).all()
    role_has_module_ids = list(role_has_module_ids)
    for module in all_modules:
        if role_has_module_ids.count(module.get('id')) > 0:
            module['checked'] = 'true'
        else:
            module['checked'] = 'false'
    return render(request, 'relate_modules_index.html', {'modules': all_modules, 'role_id': role_id})


# 角色关联权限
@require_POST
@csrf_exempt
def dorelate(request, role_id):
    # 先获取关联上的所有操作权限
    selected_module_ids = request.POST.get('selected_module_ids')
    permissions = []
    role = Role.objects.get(pk=role_id)
    for module_id in selected_module_ids.split(','):
        selected_module = Module.objects.get(pk=module_id)
        opt_value = selected_module.optValue
        permission = Permission(role=role, module=selected_module,
                                aclValue=opt_value, isValid=1,
                                createDate=timezone.now(), updateDate=timezone.now())

        permissions.append(permission)

    # 删除与该角色绑定的操作权限
    Permission.objects.filter(role__id=role_id).delete()
    # 关联选择的权限，批量插入
    Permission.objects.bulk_create(permissions)
    # 返回
    return JsonResponse({'code': 1, 'message': '操作成功！'})


# 跳转到模板
def user_index(request):
    return render(request, 'user_index.html')


# 分页查询数据
@require_GET
def select_user(request):
    # 查询的命令
    select = {'createDate': 'SELECT DATE_FORMAT(create_date, "%%Y-%%m-%%d %%H:%%i:%%s")',
              'updateDate': 'SELECT DATE_FORMAT(update_date, "%%Y-%%m-%%d %%H:%%i:%%s")'}
    queryset = User.objects.extra(select=select).values('id', 'userName', 'trueName', 'email', 'phone',
                                                        'createDate', 'updateDate').order_by('-id').all()
    name = request.GET.get('userName')
    if name:
        queryset = queryset.filter(userName__icontains=name)
    phone = request.GET.get('phone')
    if phone:
        queryset = queryset.filter(phone__icontains=phone)
    # 获取分页的参数 page page_size
    page = request.GET.get('page', 1)
    page_size = request.GET.get('rows', 10)
    # 构建分页对象
    p = Paginator(queryset, page_size)  # 传入结果集以及每页多少条
    # 分页查询结果集
    rows = p.page(page).object_list
    # 返回数据
    return JsonResponse({'rows': list(rows), 'total': p.count})


# 添加数据
@require_POST
@csrf_exempt
def add_user(request):
    # 获取角色id集合
    role_ids = request.POST.getlist('roleIds')
    is_empty(role_ids, message='请选择角色')
    # 获取参数
    user = request.POST.dict()
    del user['roleIds']
    del user['id']
    # 基本参数校验
    # TODO

    user_name = user.get('userName')
    # 用户名唯一性校验
    is_empty(user_name, message='请输入用户名')
    try:
        User.objects.get(userName=user_name)
        return JsonResponse({'code': 0, 'message': '该用户名已存在，请确认后重试！'})
    except ObjectDoesNotExist as e:
        pass
    # 密码加密
    password = user.get('password')
    is_empty(password, message='请输入密码')
    password = md5(password.encode(encoding='utf-8')).hexdigest()
    user['password'] = password
    # 添加默认字段值
    user['isValid'] = 1
    user['createDate'] = timezone.now()
    user['updateDate'] = timezone.now()
    # 添加数据
    obj = User.objects.create(**user)

    # 把角色绑定到用户往t_user_role插入数据
    user_roles = []
    for role_id in role_ids:
        role = Role.objects.get(pk=role_id)
        user_role = UserRole(user=obj, role=role, isValid=1, createDate=timezone.now(), updateDate=timezone.now())
        user_roles.append(user_role)
    UserRole.objects.bulk_create(user_roles)
    return JsonResponse({'code': 1, 'message': '添加成功！'})


# 修改用户
@require_POST
@csrf_exempt
def update_user(request):
    # 获取角色id集合
    role_ids = request.POST.getlist('roleIds')
    is_empty(role_ids, message='请选择角色')
    user = request.POST.dict()
    del user['roleIds']
    pk = user.pop('id')
    is_empty(pk, message='请选择一条记录进行修改！')
    # 基本参数校验
    user_from_db = User.objects.get(pk=pk)
    user_name = user.get('userName')
    # 唯一性校验
    if user_name != user_from_db.userName:
        try:
            User.objects.get(userName=user_name)
            return JsonResponse({'code': 0, 'message': '该用户名已存在，请确认后重试！'})
        except ObjectDoesNotExist as e:
            pass
    password = user.get('password')
    if password:
        password = md5(password.encode(encoding='utf-8')).hexdigest()
        user['password'] = password
    else:
        del user['password']
    user['updateDate'] = timezone.now()
    User.objects.filter(pk=pk).update(**user)

    # 给用户绑定角色
    # 先删除 再添加
    UserRole.objects.filter(user__id=pk).delete()
    user_roles = []
    for role_id in role_ids:
        role = Role.objects.get(pk=role_id)
        user_role = UserRole(user=user_from_db, role=role, isValid=1, createDate=timezone.now(),
                             updateDate=timezone.now())
        user_roles.append(user_role)
    UserRole.objects.bulk_create(user_roles)

    return JsonResponse({'code': 1, 'message': '修改成功！'})


# 删除用户
@require_POST
@csrf_exempt
def delete_user(request):
    ids = request.POST.get('ids')
    User.objects.filter(pk__in=ids.split(',')).update(isValid=0, updateDate=timezone.now())
    # 删除关联的角色
    queryset = UserRole.objects.filter(user__id__in=ids.split(','))
    queryset.delete()
    return JsonResponse({'code': 1, 'message': '删除成功！'})


# 获取所有的角色
def find_roles(request):
    roles = Role.objects.values('id', 'roleName').all()
    return JsonResponse(list(roles), safe=False)


# 获取用户角色id集合
def find_user_roles(request, user_id):
    user_role_id = UserRole.objects.values_list('role__id', flat=True).filter(user__id=user_id).all()
    return JsonResponse(list(user_role_id), safe=False)
