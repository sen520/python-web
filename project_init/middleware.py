"""
中间件的开发
- 响应前后操作
- 响应前后分开操作
"""
from apps import app
from flask import request, redirect


@app.before_request
def before_request(*args, **kwargs):
    # print('------before request-------')
    # print(request.path, request.remote_addr)
    pass


@app.after_request
def after_request(response):
    # print('------after request-------')
    return response


class middle:
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        # print('before @before_request')
        obj = self.wsgi_app(*args, **kwargs)
        # print('after @after_request')
        return obj
