from django.shortcuts import render, redirect
import json

# Create your views here.


def index(request):
    # 通过session判断是否登录，如果登录，就直接跳转到登陆后的页面
    user_str = request.session.get('login_user')
    if user_str:
        return redirect("index:main")
    return render(request, 'index.html')


def main(request):
    # 通过session获取用户名，如果没有，说明没有登录
    user_str = request.session.get('login_user')
    if user_str is None:
        return redirect('index:index')
    user = json.loads(user_str, encoding='utf-8')
    return render(request, 'main.html', user)
