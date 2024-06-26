"""ideatype URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include

from blog.views import AuthorView, SearchView, IndexView, CategoryView, TagView, PostDetailView
from comment.views import CommentView
from config.views import LinkListView
import ideatype.settings.base as settings
from .custom_site import custom_site
from django.contrib.sitemaps import views as sitemap_views
from blog.rss import LatestPostFeed
from blog.sitemap import PostSitemap

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('super_admin/', custom_site.urls, name='super-admin'),
    re_path('^$', IndexView.as_view(), name='index'),
    re_path('^category/(?P<category_id>\d+)$', CategoryView.as_view(), name='category-list'),
    re_path('^tag/(?P<tag_id>\d+)$', TagView.as_view(), name='tag-list'),
    re_path('^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    re_path('^links/$', LinkListView.as_view(), name='links'),
    re_path('^search/$', SearchView.as_view(), name='search'),
    re_path('^author/(?P<owner_id>\d+)$', AuthorView.as_view(), name='author'),
    re_path('^comment/$', CommentView.as_view(), name='comment'),
    re_path('^rss|feed/$', LatestPostFeed(), name='rss'),
    re_path('^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        re_path('^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns