"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = urls.py
__time__ = 2018/5/31 13:03
"""
from django.urls import path, re_path

from blog_view import views

app_name = 'blog_view'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.IndexView.as_view(), name='index'),
    # path('search/', views.search, name='search'),
    re_path(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    re_path(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^tag/(?P<pk>[0-9]+)/$', views.TagView.as_view(), name='tag'),
    # path('search/', views.search, name='search'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    path('about/', views.aboutme, name='aboutme'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
]
