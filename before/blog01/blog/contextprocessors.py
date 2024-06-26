"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = contextprocessors.py
__time__ = 2018/5/30 17:04
"""
from .models import *


def getrightinfo(request):
    # 分类方法
    from django.db.models import Count
    cate_posts = Post.objects.values('category__cname', 'category').annotate(count=Count('*')).order_by('-count')  # 分组信息
    # 归档信息
    from django.db import connection
    cursor = connection.cursor()
    arc_posts = cursor.execute(
        "select created,count('*') as count from t_post group by strftime('%Y-%m',created) order by  created desc")
    # 近期文章
    recent_posts = Post.objects.all().order_by('-id')[:3]

    return {'cate_posts': cate_posts, 'recent_posts': recent_posts, 'arc_posts': arc_posts}
