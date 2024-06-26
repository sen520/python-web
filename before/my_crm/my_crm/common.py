from django.utils.deprecation import MiddlewareMixin
from django.http.response import JsonResponse
from django.shortcuts import render
from django.core.exceptions import PermissionDenied
from functools import wraps

class ParamException(Exception):

    def __init__(self, code=0, message='系统异常，请联系管理员！'):
        self.code = code
        self.message = message

    @staticmethod
    def create_error(message):
        p = ParamException(message=message)
        return p


class CrmMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # TODO 做一个登录校验，除了登录的url地址和登录api接口，其他所有地址都必须登录
        pass

    # 处理异常机制
    def process_exception(self, request, exception):
        print(exception)
        if isinstance(exception, ParamException):
            result = {'code': exception.code, 'message': exception.message}
        if isinstance(exception, PermissionDenied):
            result = {'code': 0, 'message': exception}
        else:
            result = {'code': 0, 'message': '系统异常，请联系管理员'}

        # 校验是否是ajax请求
        if request.is_ajax():
            return JsonResponse(result)
        else:
            return render(request, "error.html", result)


# 如果为空报异常
def is_empty(value, code=0, message='系统异常，请联系管理员'):
   if value is None:
       raise ParamException(code, message)


def common_delete(request, model):
    ids = request.POST.get('ids')
    # 判断
    is_empty(ids, message="请选择记录进行删除!")

    model.objects.filter(pk__in=ids.split(',')).update(isValid=0)
    return JsonResponse({"code": 1, "message": "删除成功！"})


# 控制访问权限
def require_permission(permission):
    """验证此用户是否能访问此url permission就是访问权限"""
    def decorator(func):
        @wraps(func)
        def inner(request, *args, **kwargs):
            # 进行权限校验
            user_permissions = request.session.get('login_user_permissions')
            if not user_permissions:
                raise PermissionDenied("无权访问此地址！")
            if permission not in user_permissions:
                raise PermissionDenied("无权访问此地址！")
            return func(request, *args, **kwargs)
        return inner
    return decorator


def require_permission2(permission):
    """验证此用户是否能访问此url permission就是访问权限"""
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            # 进行权限校验
            user_permissions = request.session.get('login_user_permissions')
            if not user_permissions:
                raise PermissionDenied("无权访问此地址！")
            if permission not in user_permissions:
                raise PermissionDenied("无权访问此地址！")
            return func(request, *args, **kwargs)
        return wrapper
    return decorator

