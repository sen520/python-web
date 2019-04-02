# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from reader.models import *

# Create your views here.

#显示读者信息
def reader_view(request):
    readers = TbReader.objects.all()
    for reader in readers:
        reader.typeid = TbReadertype.objects.filter(id=reader.id)[0].name
    return render(request, 'reader.html', {'readers': readers})

#显示读者类型
def readerType_view(request):
    readertypes = TbReadertype.objects.all()
    return render(request, 'readerType.html', {'readertypes': readertypes})

#添加读者类型信息
def readerType_addview(request):
    return render(request, 'readerType_add.html')

def save_readerTypeadd(name, number):
    try:
        RT = TbReadertype.objects.get(name=name, number=number)
        RT.save()
    except:
        RT = TbReadertype.objects.create(name=name, number=number)
        RT.save()


def readerTypeaddview(request):

    name = request.POST.get('name', '')
    number = request.POST.get('number', '')

    save_readerTypeadd(name, number)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')

#添加读者信息
def reader_addview(request):
    return render(request, 'reader_add.html')


def save_readeradd(barcode, name, typeid, papertype, paperno, tel, email):
    try:
        RA = TbReader.objects.get(barcode=barcode, name=name, typeid=typeid, papertype=papertype, paperno=paperno, tel=tel, email=email)
        RA.save()
    except:
        RA = TbReader.objects.create(barcode=barcode, name=name, typeid=typeid, papertype=papertype, paperno=paperno, tel=tel, email=email)
        RA.save()

def readeraddview(request):
    barcode = request.POST.get('barcode', '')
    name = request.POST.get('name', '')
    typeid = request.POST.get('typeid', '')
    papertype = request.POST.get('papertype', '')
    paperno = request.POST.get('paperno', '')
    tel = request.POST.get('tel', '')
    email = request.POST.get('email', '')

    save_readeradd(barcode, name, typeid, papertype, paperno, tel, email)

    return HttpResponse('<script> alert("添加成功");window.close();</script>')

#读者信息删除
def reader_delview(request, delid):
    TbReader.objects.filter(id=delid).delete()

    return HttpResponse('<script> alert("删除成功");window.close();</script>')

#读者类型信息删除
def readerType_delview(request, delid):
    TbReadertype.objects.filter(id=delid).delete()

    return HttpResponse('<script> alert("删除成功");window.close();</script>')

#修改图书类型信息
def bookType_upview(request, upid):
    # 根据upid查询当前修改的图书对象信息
    booktype = TbBooktype.objects.get(id=upid)

    return render(request, 'bookType_up.html', {'booktype': booktype})
#修改读者类型信息
def readerType_upview(request, upid):
    readertype = TbReadertype.objects.get(id=upid)
    return render(request, 'readerType_up.html', {'readertype': readertype})



def readerTypeupview(request, upid):
    name = request.POST.get('name', '')
    number = request.POST.get('number', '')
    TbReadertype.objects.filter(id=upid).update(name=name, number=number)

    return HttpResponse('<script> alert("添加成功");window.close();</script>')

#修改读者信息
def reader_upview(request, upid):
    reader = TbReader.objects.get(id=upid)

    return render(request, 'reader_up.html', {'reader': reader})

def readerupview(request, upid):
    barcode = request.POST.get('barcode', '')
    name = request.POST.get('name', '')
    typeid = request.POST.get('typeid', '')
    papertype = request.POST.get('papertype', '')
    paperno = request.POST.get('paperno', '')
    tel = request.POST.get('tel', '')
    email = request.POST.get('email', '')

    TbReader.objects.filter(id=upid).update(barcode=barcode, name=name, typeid=typeid, papertype=papertype, paperno=paperno, tel=tel, email=email)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')