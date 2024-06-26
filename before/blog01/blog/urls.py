"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = urls.py
__time__ = 2018/5/30 15:27
"""
from django.urls import path, re_path

from blog import views

urlpatterns = [
    path('', views.index_view),
    path('page/<int:page_id>', views.index_view),
    path('post/<int:postid>', views.post_view),
    path('category/<int:categoryid>', views.cate_view),
    path('archive/', views.archive_view),
    re_path(r'^archive/(\d{4})/(\d{2})$', views.archive_view),
    path('aboutme/', views.aboutme_view),
    path('search/', views.search_view),
]
