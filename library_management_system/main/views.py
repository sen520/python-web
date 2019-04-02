# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.db import connection
# Create your views here.


def main_view(request):

    cursor = connection.cursor()
    cursor.execute("SELECT barcode,bookname,typename,NAME,pubname,author,price,COUNT(*) c FROM tb_publishing tb_pub RIGHT JOIN(SELECT barcode,bookname,typename,NAME,isbn,author,price FROM tb_bookcase tb_case RIGHT JOIN(SELECT barcode,bookname,typename,bookcase,isbn,author,price FROM tb_booktype tb_type RIGHT JOIN (SELECT barcode,bookname,typeid,bookcase,isbn,author,price FROM tb_bookinfo tb_book RIGHT JOIN tb_borrow tb_b ON tb_book.id=tb_b.bookid) book ON tb_type.id=book.typeid) tb_all ON tb_case.id=tb_all.bookcase) tb ON tb_pub.isbn=tb.isbn GROUP BY barcode ORDER BY c DESC")
    datas = cursor.fetchall()



    return render(request, 'main.html', {'datas': datas})