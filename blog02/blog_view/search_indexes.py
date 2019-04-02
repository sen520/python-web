"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = search_indexes.py
__time__ = 2018/5/31 20:53
"""
from haystack import indexes
from .models import Post


class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.all()