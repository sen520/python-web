# coding=utf-8

from django.conf.urls import url

from bookBorrow import views

urlpatterns = [
    url(r'^bookBorrow.html$', views.bookBorrow_view),
    url(r'^savebook$', views.saveBorrow_view),
    url(r'^bookRenew.html$', views.bookRenew_view),
    url(r'^bookBack.html$', views.bookBack_view),
    url(r'^bookrenew/(\d+)', views.bookrenew_view),
    url(r'^bookback/(\d+)', views.bookback_view),
]