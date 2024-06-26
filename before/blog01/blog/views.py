# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator
from .models import *


# Create your views here.
def get_post_by_num(num):
    # 转换int类型
    num = int(num)
    page_posts = Paginator(Post.objects.all().order_by("-created"), per_page=2)

    # 判断当前页是否越界
    if num <= 0:
        num = 1

    if num > page_posts.num_pages:
        num = page_posts.num_pages

    # 生成页码数
    # 起始数
    start = ((num - 1) // 10) * 10 + 1

    # 末尾数
    end = start + 10

    # 判断end是否越界
    if end > page_posts.num_pages:
        end = page_posts.num_pages + 1

    return page_posts.page(num), range(start, end)


def get_postbyid(postid):
    return Post.objects.get(id=postid)


def index_view(request, page_id='1'):
    # 查询第一页的数据
    page_posts, page_range = get_post_by_num(page_id)

    return render(request, 'index.html', {'page_posts': page_posts, 'page_range': page_range})


def post_view(request, postid):
    post = get_postbyid(postid)
    return render(request, 'detail.html', {'post': post})


def cate_view(request, categoryid):
    cate_posts = Post.objects.filter(category_id=categoryid).order_by('-created')
    return render(request, 'archive.html', {'archive_posts': cate_posts})


def archive_view(request, year=None, month=None):
    if year and month:
        archive_posts = Post.objects.filter(created__year=year, created__month=month).order_by('-created')
    else:
        archive_posts = Post.objects.all().order_by('-created')
    return render(request, 'archive.html', {'archive_posts': archive_posts})


def aboutme_view(request):
    return render(request,'aboutme.html')


def search_view(request):
    from haystack.query import SearchQuerySet
    from haystack.query import SQ

    # 获取请求参数
    keywords = request.GET.get('q', '')

    search_posts = SearchQuerySet().filter(SQ(title=keywords) | SQ(content=keywords))

    s_posts = []

    for s_p in search_posts:
        s_posts.append(s_p.object)

    return render(request,'archive.html',{'archive_posts':s_posts})