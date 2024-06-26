# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from .models import *

def login_check(username, password):
    for user in TbManager.objects.all():
        if username == user.name:
            if password == user.pwd:
                return 1
            else:
                return 2
    else:
        return 3


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('name')
        password = request.POST.get('pwd')

        check = login_check(username, password)

        request.session['loginuser'] = username



        return render(request, 'login.html', {'username': username, 'check': check})