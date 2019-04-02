"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = urls.py
__time__ = 2018/5/31 18:57
"""
from django.urls import path,re_path

from comments import views

app_name = 'comments'
urlpatterns = [
    re_path(r'^comment/post/(?P<post_pk>[0-9]+)/$', views.post_comment, name='post_comment'),
]