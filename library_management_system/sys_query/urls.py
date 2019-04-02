from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^borrowQuery.html', views.borrowQuery_view),
    url(r'^bremind.html', views.bremind_view),
    url(r'^bookQuery.html', views.bookQuery_view),

]