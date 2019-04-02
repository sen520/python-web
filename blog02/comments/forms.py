"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = forms.py
__time__ = 2018/5/31 18:48
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
