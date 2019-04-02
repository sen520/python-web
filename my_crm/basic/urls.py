from django.urls import path
from . import views

app_name = 'basic'
urlpatterns = [

    path('datadic_list/', views.datadic_list, name='datadic_list'),
    path('datadic_index/', views.datadic_index, name='datadic_index'),
    path('select_datadic/', views.select_datadic, name='select_datadic'),
    path('find_all/', views.find_all, name='find_all'),
    path('add_datadic/', views.add_datadic, name='add_datadic'),
    path('update_datadic/', views.update_datadic, name='update_datadic'),
    path('delete_datadic/', views.delete_datadic, name='delete_datadic'),

    path('product_index/', views.product_index, name='product_index'),
    path('select_product/', views.select_product, name='select_product'),

]
