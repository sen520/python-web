"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = search_indexes.py.py
__time__ = 2018/5/30 17:33
"""

# 注意格式
from haystack import indexes
from blog.models import *


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # 给title设置索引
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created')
