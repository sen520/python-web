from django.urls import path

from . import views

app_name = 'sales'
urlpatterns = [
    # ------------------------营销机会管理-------------------------------
    path('index/',views.index,name='index'),
    path('select_for_page/',views.select_for_page,name='select_for_page'),
    path('save_sale_chance/',views.save_sale_chance,name='save_sale_chance'),
    path('update_sale_chance/',views.update_sale_chance,name='update_sale_chance'),
    path('delete_sale_chances/',views.delete_sale_chances,name='delete_sale_chances'),

    # ------------------------客户开发计划-------------------------------
    path('plan_index/', views.plan_index, name='plan_index'),
    path('<int:sale_chance_id>/cus_dev_index/', views.cus_dev_index, name='cus_dev_index'),
    path('<int:sale_chance_id>/cus_dev_list/', views.cus_dev_list, name='cus_dev_list'),
    path('<int:sale_chance_id>/cus_dev_add/', views.cus_dev_add, name='cus_dev_add'),
    path('<int:sale_chance_id>/cus_dev_update/', views.cus_dev_update, name='cus_dev_update'),
    path('<int:sale_chance_id>/cus_dev_delete/', views.cus_dev_delete, name='cus_dev_delete'),
    path('<int:sale_chance_id>/update_dev_result/', views.update_dev_result, name='update_dev_result'),
]