from django.urls import path
from . import views

app_name = 'serve'
urlpatterns = [

    path('index/<str:template>/', views.index, name='index'),
    path('create_index/', views.create_index, name='create_index'),
    path('add/', views.add, name='add'),
    path('server_assign/', views.server_assign, name='server_assign'),
    path('select_for_page/', views.select_for_page, name='select_for_page'),
    path('update/', views.update, name='update'),
]
