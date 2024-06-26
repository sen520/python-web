# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from books.models import *
# from books import models
# Create your views here.
#显示图书类型信息
def bookType_view(request):
    Type_books = TbBooktype.objects.all()

    return render(request, 'bookType.html', {'Type_books': Type_books})

#显示图书信息
def book_view(request):

    info_books = TbBookinfo.objects.all()
    for book in info_books:
        book.typeid = TbBooktype.objects.filter(id=book.typeid)[0].typename
        book.bookcase = TbBookcase.objects.filter(id=book.bookcase)[0].name

    return render(request, 'book.html', {'info_books': info_books})

#添加图书类型信息
def bookType_addview(request):

    return render(request, 'bookType_add.html')


#添加图书类型信息
def save_bookTypeadd(typename, days):
    try:
        BT = TbBooktype.objects.get(typename=typename, days=days)
        BT.save()
    except:
        BT = TbBooktype.objects.create(typename=typename, days=days)
        BT.save()
def bookTypeaddview(request):
    typename = request.POST.get('typename', '')
    days = request.POST.get('days', '')
    # print(typename, days)
    save_bookTypeadd(typename, days)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')

#添加图书信息
def book_addview(request):
    return render(request, 'book_add.html')

def save_bookadd(barcode, bookname, typeid, author, bookcase):
    try:
        BT = TbBookinfo.objects.get(barcode=barcode, bookname=bookname, typeid=typeid, author=author, bookcase=bookcase)
        BT.save()
    except:
        BT = TbBookinfo.objects.create(barcode=barcode, bookname=bookname, typeid=typeid, author=author, bookcase=bookcase)
        BT.save()

def bookaddview(request):
    barcode = request.POST.get('barcode', '')
    bookname = request.POST.get('bookname', '')
    typeid = request.POST.get('typeid', '')
    author = request.POST.get('author', '')
    bookcase = request.POST.get('bookcase', '')
    # print(barcode, bookname, typeid, author, bookcase)

    save_bookadd(barcode, bookname, typeid, author, bookcase)
    return HttpResponse('<script> alert("添加成功");window.close();</script>')

#图书信息删除
def book_delview(request, delid):
    # print delid
    TbBookinfo.objects.filter(id=delid).delete()

    return HttpResponse('<script> alert("删除成功");window.close();</script>')

#图书类型信息删除
def bookType_delview(request, delid):
    TbBooktype.objects.filter(id=delid).delete()

    return HttpResponse('<script> alert("删除成功");window.close();</script>')

#修改图书信息
def book_upview(request, upid):
    book = TbBookinfo.objects.get(id=upid)
    # print upid
    return render(request, 'book_up.html', {'book': book})


def bookupview(request, upid):
    # print upid
    barcode = request.POST.get('barcode', '')
    bookname = request.POST.get('bookname', '')
    typeid = request.POST.get('typeid', '')
    author = request.POST.get('author', '')
    bookcase = request.POST.get('bookcase', '')
    # print bookname
    TbBookinfo.objects.filter(id=upid).update(barcode=barcode, bookname=bookname, typeid=typeid, author=author, bookcase=bookcase)

    return HttpResponse('<script> alert("修改成功");window.close();</script>')

#修改图书类型信息
def bookType_upview(request, upid):
    # 根据upid查询当前修改的图书对象信息
    booktype = TbBooktype.objects.get(id=upid)

    return render(request, 'bookType_up.html', {'booktype': booktype})

def bookTypeupview(request, upid):
    typename = request.POST.get('typename', '')
    days = request.POST.get('days', '')
    TbBooktype.objects.filter(id=upid).update(typename=typename, days=days)

    return HttpResponse('<script> alert("修改成功");window.close();</script>')
