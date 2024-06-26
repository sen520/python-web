from django.urls import path
from . import views

app_name = 'system'
urlpatterns = [
    # -----------系统------------- #
    path('login/', views.login, name='login'),
    path('update_password/', views.update_password, name='update_password'),
    path('logout/', views.logout, name='logout'),
    path('find_customer_manager/', views.find_customer_manager, name='find_customer_manager'),

    # -----------资源------------- #
    path('module_index/', views.module_index, name='module_index'),
    path('select_module/', views.select_module, name='select_module'),
    path('findByGrade/', views.find_by_grade, name='findByGrade'),
    path('add_module/', views.add_module, name='add_module'),
    path('update_module/', views.update_module, name='update_module'),
    path('delete_module/', views.delete_module, name='delete_module'),

    # -----------角色------------- #
    path('role_index/', views.role_index, name='role_index'),
    path('select_role/', views.select_role, name='select_role'),
    path('add_role/', views.add_role, name='add_role'),
    path('update_role/', views.update_role, name='update_role'),
    path('delete_role/', views.delete_role, name='delete_role'),
    path('<int:role_id>/relate_modules_index/', views.relate_modules_index, name='relate_modules_index'),
    path('<int:role_id>/dorelate/', views.dorelate, name='dorelate'),
    path('find_roles/', views.find_roles, name='find_roles'),
    path('test_ztree/', views.test_ztree, name='test_ztree'),

    # -----------用户------------- #
    path('user_index/', views.user_index, name='user_index'),
    path('select_user/', views.select_user, name='select_user'),
    path('add_user/', views.add_user, name='add_user'),
    path('update_user/', views.update_user, name='update_user'),
    path('delete_user/', views.delete_user, name='delete_user'),
    path('<int:user_id>/find_user_roles/', views.find_user_roles, name='find_user_roles'),

]
