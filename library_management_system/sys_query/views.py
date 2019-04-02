# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import *

from django.http.response import HttpResponse

import datetime
from datetime import timedelta
# Create your views here.
def query_by_barcode(key):
    borrows = []
    bors = {}
    bookid = TbBookinfo.objects.filter(barcode=key)[0].id
    borrow = TbBorrow.objects.filter(bookid=bookid)
    for bor in borrow:

        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')

        if bor.ifback == 0:
            bors['ifback'] = '未归还'
        else:
            bors['ifback'] = '已归还'
        borrows.append(bors.copy())
    return borrows

def query_by_bookname(key):
    borrows = []
    bors = {}

    bookid = TbBookinfo.objects.filter(bookname=key)[0].id
    borrow = TbBorrow.objects.filter(bookid=bookid)
    for bor in borrow:
        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')
        if bor.ifback == 0:
            bors['ifback'] = '未归还'
        else:
            bors['ifback'] = '已归还'
        borrows.append(bors.copy())
    return borrows




def query_by_readerbarcode(key):
    borrows = []
    bors = {}

    readerid = TbReader.objects.filter(barcode=key)[0].id
    borrow = TbBorrow.objects.filter(readerid=readerid)
    for bor in borrow:
        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')
        if bor.ifback == 0:
            bors['ifback'] = '未归还'
        else:
            bors['ifback'] = '已归还'
        borrows.append(bors.copy())
    return borrows


def query_by_readername(key):
    borrows = []
    bors = {}

    readerid = TbReader.objects.filter(name=key)[0].id
    borrow = TbBorrow.objects.filter(readerid=readerid)
    for bor in borrow:
        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')
        if bor.ifback == 0:
            bors['ifback'] = '未归还'
        else:
            bors['ifback'] = '已归还'
        borrows.append(bors.copy())
    return borrows


def query_by_date(sdate, edate):
    borrows = []
    bors = {}

    borrow = TbBorrow.objects.filter(borrowtime__range=(sdate, edate))
    for bor in borrow:
        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')
        if bor.ifback == 0:
            bors['ifback'] = '未归还'
        else:
            bors['ifback'] = '已归还'
        borrows.append(bors.copy())
    return borrows


def query_by_barcode_date(key, sdate, edate):
    borrows = []
    borrow = query_by_date(sdate, edate)
    for bor in borrow:
        if key == bor['barcode']:
            borrows.append(bor)
    return borrows


def query_by_bookname_date(key, sdate, edate):
    borrows = []
    borrow = query_by_date(sdate, edate)
    for bor in borrow:
        if key == bor['bookname']:
            borrows.append(bor)
    return borrows


def query_by_readerbarcode_date(key, sdate, edate):
    borrows = []
    borrow = query_by_date(sdate, edate)
    for bor in borrow:
        if key == bor['readerbarcode']:
            borrows.append(bor)
    return borrows


def query_by_readername_date(key, sdate, edate):
    borrows = []
    borrow = query_by_date(sdate, edate)
    for bor in borrow:
        if key == bor['readername']:
            borrows.append(bor)
    return borrows


def borrowQuery_view(request):
    if request.method == 'GET':
        return render(request, 'borrowQuery.html')
    else:
        key = request.POST.get('key')

        a = request.POST.get('flag')
        b = request.POST.get('flag2')

        sdate = request.POST.get('sdate')
        edate = request.POST.get('edate')

        if a =='a' and b == None:
            if request.POST.get('f') == 'barcode':
                for book in TbBookinfo.objects.all():
                    if book.barcode == key:

                        book_info = query_by_barcode(key)
                        return render(request, 'borrowQuery.html', {'key': key, 'book_info': book_info})
                else:
                    return HttpResponse('<script>alert("没有找到该图书");window.history.go(-1);</script>')

            elif request.POST.get('f') == 'bookname':
                for book in TbBookinfo.objects.all():
                    if book.bookname == key:
                        book_info = query_by_bookname(key)
                        return render(request, 'borrowQuery.html', {'book_info': book_info})
                else:
                    return HttpResponse('<script>alert("没有找到该图书");window.history.go(-1);</script>')

            elif request.POST.get('f') == 'readerbarcode':
                for reader in TbReader.objects.all():
                    if reader.barcode == key:
                        book_info = query_by_readerbarcode(key)
                        return render(request, 'borrowQuery.html', {'book_info': book_info})
                else:
                    return HttpResponse('<script>alert("没有找到该读者");window.history.go(-1);</script>')
            elif request.POST.get('f') == 'readername':
                for reader in TbReader.objects.all():
                    if reader.name == key:
                        book_info = query_by_readername(key)
                        return render(request, 'borrowQuery.html', {'book_info': book_info})
                else:
                    return HttpResponse('<script>alert("没有找到该读者");window.history.go(-1);</script>')

        if a == None and b == 'b':

            if sdate < edate:
                book_info = query_by_date(sdate, edate)
                return render(request, 'borrowQuery.html', {'key': key, 'book_info': book_info})
            else:
                return HttpResponse('<script>alert("日期应该从小到大");window.history.go(-1);</script>')

        if a =='a' and b == 'b':
            if sdate < edate:
                if request.POST.get('f') == 'barcode':
                    for book in TbBookinfo.objects.all():
                        if book.barcode == key:
                            book_info = query_by_barcode_date(key, sdate, edate)

                            return render(request, 'borrowQuery.html', {'key': key, 'book_info': book_info})
                    else:
                        return HttpResponse('<script>alert("没有找到该图书");window.history.go(-1);</script>')

                elif request.POST.get('f') == 'bookname':
                    for book in TbBookinfo.objects.all():
                        if book.bookname == key:
                            book_info = query_by_bookname_date(key, sdate, edate)
                            return render(request, 'borrowQuery.html', {'book_info': book_info})
                    else:
                        return HttpResponse('<script>alert("没有找到该图书");window.history.go(-1);</script>')

                elif request.POST.get('f') == 'readerbarcode':
                    for reader in TbReader.objects.all():
                        if reader.barcode == key:
                            book_info = query_by_readerbarcode_date(key, sdate, edate)
                            return render(request, 'borrowQuery.html', {'book_info': book_info})
                    else:
                        return HttpResponse('<script>alert("没有找到该读者");window.history.go(-1);</script>')
                elif request.POST.get('f') == 'readername':
                    for reader in TbReader.objects.all():
                        if reader.name == key:
                            book_info = query_by_readername_date(key, sdate, edate)
                            return render(request, 'borrowQuery.html', {'book_info': book_info})
                    else:
                        return HttpResponse('<script>alert("没有找到该读者");window.history.go(-1);</script>')
            else:
                return HttpResponse('<script>alert("日期应该从小到大");window.history.go(-1);</script>')

        if a == None and b == None:
            return HttpResponse('<script>alert("请选择一种查询方式");window.history.go(-1);</script>')


def bremind():
    borrows = []
    bors = {}

    T = datetime.date.today()-timedelta(days=2)
    borrow = TbBorrow.objects.filter(ifback=0, backtime__lt=T)


    for bor in borrow:
        bors['barcode'] = TbBookinfo.objects.filter(id=bor.bookid)[0].barcode
        bors['bookname'] = TbBookinfo.objects.filter(id=bor.bookid)[0].bookname
        bors['readerbarcode'] = TbReader.objects.filter(id=bor.readerid)[0].barcode
        bors['readername'] = TbReader.objects.filter(id=bor.readerid)[0].name
        bors['borrowtime'] = bor.borrowtime.strftime('%Y-%m-%d')
        bors['backtime'] = bor.backtime.strftime('%Y-%m-%d')
        # if bor.ifback == 0:
        #     if (T-bor.backtime).days>48:
        borrows.append(bors.copy())
    return borrows
def bremind_view(request):
    bremind()
    return render(request, 'bremind.html', {'bremind': bremind})


def query_by_querytype_barcode(key):
    for tb in TbBookinfo.objects.all():
        if key == tb.barcode:
            book = TbBookinfo.objects.filter(barcode=key)
            return book
    else:
        return False


def query_by_querytype_typename(key):
    for tp in TbBooktype.objects.all():
        if key == tp.typename:
            book = TbBookinfo.objects.filter(typeid=tp.id)
            return book
    else:
        return False


def query_by_querytype_bookname(key):
    for tb in TbBookinfo.objects.all():
        if key == tb.bookname:
            book = TbBookinfo.objects.filter(bookname=key)
            return book
    else:
        return False


def query_by_querytype_author(key):
    for tb in TbBookinfo.objects.all():
        if key == tb.author:
            book = TbBookinfo.objects.filter(author=key)
            return book
    else:
        return False


def query_by_querytype_publishing(key):
    for tb in TbPublishing.objects.all():
        if key == tb.pubname:
            book = TbBookinfo.objects.filter(isbn=tb.isbn)
            return book
    else:
        return False


def query_by_querytype_bookcasename(key):
    for tb in TbBookcase.objects.all():
        if key == tb.name:
            book = TbBookinfo.objects.filter(bookcase=tb.id)
            return book
    else:
        return False


def bookQuery_view(request):
    if request.method == 'GET':
        return render(request, 'bookQuery.html')
    else:
        querytype = request.POST.get('f')
        key = request.POST.get('key')
        if querytype == 'barcode':
            book = query_by_querytype_barcode(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到此书");window.history.go(-1);</script>')

        if querytype == 'typename':
            book = query_by_querytype_typename(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到此类的书");window.history.go(-1);</script>')

        if querytype == 'bookname':
            book = query_by_querytype_bookname(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到此书");window.history.go(-1);</script>')

        if querytype == 'author':
            book = query_by_querytype_author(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到结果");window.history.go(-1);</script>')

        if querytype == 'publishing':
            book = query_by_querytype_publishing(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到此出版社的书");window.history.go(-1);</script>')
            
        if querytype == 'bookcasename':
            book = query_by_querytype_bookcasename(key)
            if book:
                for b in book:
                    b.typeid = TbBooktype.objects.filter(id=b.typeid)[0].typename
                    b.isbn = TbPublishing.objects.filter(isbn=b.isbn)[0].pubname
                    b.bookcase = TbBookcase.objects.filter(id=b.bookcase)[0].name
                return render(request, 'bookQuery.html', {'key': key, 'book': book})
            else:
                return HttpResponse('<script>alert("未查询到此书架的书");window.history.go(-1);</script>')