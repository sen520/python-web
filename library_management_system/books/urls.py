from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^bookType.html', views.bookType_view),
    url(r'^bookType.doaction=bookTypeDel&ID=(\d+)', views.bookType_delview),
    url(r'^updateBookType/ID=(\d+)', views.bookType_upview),
    url(r'^updateBookType/bookTypeup.html/(\d+)', views.bookTypeupview),
    url(r'^book.html', views.book_view),
    url(r'^book.doaction=bookDel&ID=(\d+)', views.book_delview),
    url(r'^book.doaction=bookModifyQuery&ID=(\d+)', views.book_upview),
    url(r'^bookup.html/(\d+)', views.bookupview),
    url(r'^bookType_add.jsp', views.bookType_addview),
    url(r'^bookTypeadd.html', views.bookTypeaddview),
    url(r'^book_add.jsp', views.book_addview),
    url(r'^bookadd.html', views.bookaddview),


]