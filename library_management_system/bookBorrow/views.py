# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import response
from django.shortcuts import render
from .models import *

from django.http.response import HttpResponse

import datetime

# Create your views here.



def query_reader(barcode):
    for reader in TbReader.objects.all():

        if reader.barcode == barcode:
            return reader
    else:
        return False


def query_book_by_code(bookinfo):
    if bookinfo:
        for book in TbBookinfo.objects.filter(del_field=0):
            if book.barcode == bookinfo:
                return book
        else:
            return '没有找到该图书'
    else:
        return None


def query_book_by_name(bookinfo):
    if bookinfo:
        for book in TbBookinfo.objects.filter(del_field=0):
            if book.bookname == bookinfo:
                return book
        else:
            return '没有找到该图书'
    else:
        return None


def query_readertype(reader):
    return TbReadertype.objects.filter(id=reader.typeid)[0]

def query_bookcount(reader):
    from django.db.models import Count
    return  query_readertype(reader).number - TbBorrow.objects.filter(readerid=reader.id, ifback=0).aggregate(c=Count('*')).get('c')


def get_Nowdate():

    # return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d')


def query_backdate(book):
    now = datetime.datetime.now()
    day = TbBooktype.objects.filter(id=book.typeid)[0].days
    delta = datetime.timedelta(days=day)
    back_date = now + delta
    return back_date.strftime('%Y-%m-%d')


def get_publishing(book):
    publishing = TbPublishing.objects.filter(isbn=book.isbn)[0].pubname
    return publishing


def get_bookcase(book):
    bookcase = TbBookcase.objects.filter(id=book.bookcase)[0].name
    return bookcase


def bookBorrow_view(request):
    if request.method == 'GET':
        return render(request, 'bookBorrow.html')
    else:
        barcode = request.POST.get('barcode')

        # 查询读者

        reader = query_reader(barcode)


        if reader:
            # 查询读者类型
            readertype = query_readertype(reader)

            # 查询可借图书总数
            readercount = query_bookcount(reader)

            bookinfo = request.POST.get('inputkey')

            # 获取图书
            if request.POST.get('f') == 'barcode':
                book = query_book_by_code(bookinfo)

            else :
                book = query_book_by_name(bookinfo)

            nowdate = None
            backdate = None
            publishing = None
            bookcase = None

            if book and book != '没有找到该图书':
                # 获取当前日期
                nowdate = get_Nowdate()
                # 计算应还时间
                backdate = query_backdate(book)

                # 获取出版社
                publishing = get_publishing(book)

                # 获取书架
                bookcase = get_bookcase(book)

            return render(request, 'bookBorrow.html', {'reader': reader, 'readertype': readertype, 'book': book, 'readercount':readercount, 'nowdate': nowdate, 'backdate': backdate, 'publishing': publishing, 'bookcase': bookcase })

        else:
            return HttpResponse('<script>alert("没有找到该读者"); window.location.href="bookBorrow.html";</script>')


def saveBorrow(readerid, book, borrowtime, backtime, operator):
    s = TbBorrow.objects.create(readerid=readerid, bookid=book.id, borrowtime=borrowtime, backtime=backtime, operator=operator, ifback=0)
    s.save()


def saveBorrow_view(request):
    # 获取读者id
    barcode = request.POST.get('barcode')
    readerid = query_reader(barcode).id

    # 获取图书id
    bookinfo = request.POST.get('inputkey')
    if request.POST.get('f') == 'barcode':
        book = query_book_by_code(bookinfo)

    else:
        book = query_book_by_name(bookinfo)

    # 获取借还日期
    borrowtime = get_Nowdate()
    backtime = query_backdate(book)

    # 获取操作员
    operator = request.session.get('loginuser')

    saveBorrow(readerid, book, borrowtime, backtime, operator)

    return HttpResponse('<script>alert("完成借阅"); window.location.href="bookBorrow.html";</script>')


def query_books(id):
    books = []
    tborrow = {}
    tb = TbBorrow.objects.filter(readerid=id, ifback=0)
    for book in tb:
        b = TbBookinfo.objects.filter(id=book.bookid)[0]
        tborrow['id'] = book.id
        tborrow['bookname'] = b.bookname
        tborrow['borrowtime'] = book.borrowtime.strftime('%Y-%m-%d')
        tborrow['backtime'] = book.backtime.strftime('%Y-%m-%d')
        tborrow['publishing'] = get_publishing(b)
        tborrow['bookcase'] = get_bookcase(b)
        tborrow['price'] = b.price

        books.append(tborrow.copy())
    return books

def bookRenew_view(request):
    if request.method == 'GET':
        return render(request, 'bookRenew.html')
    else:
        barcode = request.POST.get('barcode')

        # 查询读者
        reader = query_reader(barcode)

        if reader:
            # 查询读者类型
            readertype = query_readertype(reader)

            # 查询可借图书总数
            readercount = query_bookcount(reader)

            # 获取图书

            books = query_books(reader.id)


            return render(request, 'bookRenew.html',
                          {'reader': reader, 'readertype': readertype, 'readercount': readercount, 'books': books})

        else:
            return HttpResponse('<script>alert("没有找到该读者"); window.location.href="bookRenew.html";</script>')


def bookBack_view(request):
    if request.method == 'GET':
        return render(request, 'bookBack.html')
    else:
        barcode = request.POST.get('barcode')

        # 查询读者
        reader = query_reader(barcode)

        if reader:
            # 查询读者类型
            readertype = query_readertype(reader)

            # 查询可借图书总数
            readercount = query_bookcount(reader)

            # 获取图书

            books = query_books(reader.id)


            return render(request, 'bookBack.html',
                          {'reader': reader, 'readertype': readertype, 'readercount': readercount, 'books': books})

        else:
            return HttpResponse('<script>alert("没有找到该读者"); window.location.href="bookBack.html";</script>')


def bookrenew_view(request, id):

    bookid = TbBorrow.objects.filter(id=id)[0].bookid

    book = TbBookinfo.objects.filter(id=bookid)[0]

    days = TbBooktype.objects.filter(id=book.bookcase)[0].days

    old_back_time = TbBorrow.objects.filter(id=id)[0].backtime

    delta = datetime.timedelta(days=days)

    back_time = old_back_time + delta

    TbBorrow.objects.filter(id=id).update(backtime=back_time)

    return HttpResponse('<script> alert("完成续借"); window.history.go(-1);</script>')


def save_giveback(readerid, bookid, back_time, operator):
    give_back = TbGiveback.objects.create(readerid=readerid, bookid=bookid, backtime=back_time, operator=operator)
    give_back.save()


def bookback_view(request, id):

    readerid = TbBorrow.objects.filter(id=id)[0].readerid

    bookid = TbBorrow.objects.filter(id=id)[0].bookid

    book = TbBookinfo.objects.filter(id=bookid)[0]

    operator = request.session.get('loginuser')

    back_time = datetime.datetime.now().strftime('%Y-%m-%d')

    TbBorrow.objects.filter(id=id).update(ifback=1)

    save_giveback(readerid, bookid, back_time, operator)

    return HttpResponse('<script> alert("完成归还"); window.history.go(-1);</script>')



