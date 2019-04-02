# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse

from sys_set.models import TbManager, TbBookcase, TbPurview
from . import models

# Create your views here.
def modify_view(request):
    return render(request,'library_modify.html')

def libraryModify_view(request):
    libraryName = request.POST.get('libraryname','')
    curato = request.POST.get('curato','')
    tel = request.POST.get('tel','')
    address = request.POST.get('address','')
    email = request.POST.get('email','')
    url = request.POST.get('url','')
    created = request.POST.get('createDate', '')
    introduce = request.POST.get('introduce','')
    models.save_library(libraryName,curato,tel,address,email,url,introduce,created)
    return HttpResponse('<script> alert("保存成功");window.location.href="library_modify.html";</script>')

def main_view(request):
    return render(request,'main.html')

def manager_view(request):
    manages = TbManager.objects.all()
    checked = ''
    pulists = []
    for m in manages:
        t= TbPurview.objects.filter(id=m.id)[0]
        if m.id == t.id:
            t.name = m.name

        if t.sysset == 1:
            t.sysset = 'checked'
        else:
            t.sysset =  ''
        if t.readerset == 1:
            t.readerset = 'checked'
        else:
            t.readerset = ''
        if t.bookset == 1:
            t.bookset = 'checked'
        else:
            t.bookset = ''
        if t.borrowback == 1:
            t.borrowback = 'checked'
        else:
            t.borrowback = ''
        if t.sysquery == 1:
            t.sysquery = 'checked'
        else:
            t.sysquery = ''
        pulists.append(t)

    return render(request,'manager.html',{'manages':manages,'pulists':pulists} )

def pm_view(request):
    return render(request,'parameter_modify.html')

def bookcase_view(request):
    books = TbBookcase.objects.all()
    return render(request,'bookcase.html',{'books':books})

def manage_view(request):
    name = request.POST.get('name','')
    pwd = request.POST.get('pwd','')
    models.save_manage(name,pwd)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')

def add_view(request):
    return render(request, 'manage.html')

def parameter_view(request):
    cost = request.POST.get('cost','')
    validity = request.POST.get('validity','')
    models.save_parameter(cost,validity)
    return HttpResponse('<script> alert("保存成功");window.location.href="parameter_modify.html";</script>')

def bookadd_view(request):
    return render(request,'bookadd.html')

def bookad_view(request):
    name = request.POST.get('name','')
    models.save_bookcase(name)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')

def purview_view(request,id):
    manages = TbManager.objects.filter(id=id)[0]
    manages_tp = TbPurview.objects.filter(id=id)[0]
    return render(request,'update.html',{'manages': manages, 'manages_tp': manages_tp} )


def update_view(request,id):
    sysset = request.POST.get('sysset')
    readerset = request.POST.get('readerset')
    bookset = request.POST.get('bookset')
    borrowback = request.POST.get('borrowback')
    sysquery = request.POST.get('sysquery')

    s = sysset
    if s == 'on':
        s=1
    else:
        s=0
    r =readerset
    if r == 'on':
        r=1
    else:
        r=0
    b = bookset
    if b == 'on':
        b=1
    else:
        b=0
    w = borrowback
    if w == 'on':
        w = 1
    else:
        w = 0
    q = sysquery
    if q == 'on':
        q = 1
    else:
        q = 0
    models.save_purview(id,s,r,b,w,q)
    return HttpResponse('<script> alert("修改成功");window.close();</script>')


def del_view(request,delid):
    TbPurview.objects.filter(id = delid).delete()
    TbManager.objects.filter(id = delid).delete()
    return HttpResponse('<script> alert("删除成功");window.history.go(-1);</script>')



def dell_view(request,delid):
    TbBookcase.objects.filter(id = delid).delete()
    return HttpResponse('<script> alert("删除成功");window.history.go(-1);</script>')


def updet_view(request,id):
    name = request.POST.get('name')
    models.save_book(id,name)
    return HttpResponse('<script> alert("修改成功");window.close();</script>')


def updete_view(request,id):
    books = TbBookcase.objects.filter(id=id)[0]
    return render(request,'updatebook.html',{'books':books})