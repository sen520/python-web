# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.http.response import HttpResponse
# Create your views here.
def pwd_modify(user, password, pwd, pwd1):
    if pwd == pwd1:
        if password == pwd:
            return '<script> alert("新密码不能与旧密码一样"); window.history.go(-1);</script>'
        else:
            TbManager.objects.filter(name=user).update(pwd=pwd)
            return '<script> alert("更改口令成功"); window.history.go(-1);</script>'
    else:
        return '<script> alert("俩次输入密码不一致"); window.history.go(-1);</script>'

def pwdModify_view(request):
    if request.method == 'GET':
        user = request.session.get('loginuser')
        password = TbManager.objects.filter(name=user)[0].pwd

        return render(request, 'pwd_Modify.html', {'password': password})
    if request.method == 'POST':
        user = request.POST.get('name')
        password = TbManager.objects.filter(name=user)[0].pwd
        pwd = request.POST.get('pwd')
        pwd1 = request.POST.get('pwd1')

        str = pwd_modify(user, password, pwd, pwd1)

        return HttpResponse(str)
