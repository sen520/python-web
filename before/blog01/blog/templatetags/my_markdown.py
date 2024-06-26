"""
__author__ = zs
__contact__ = sen0117@163.com
__file__ = my_markdown.py
__time__ = 2018/5/30 17:23
"""
from django.template import Library

register = Library()


@register.filter
def md(value):
    import markdown
    return markdown.markdown(value)
