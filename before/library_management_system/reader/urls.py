from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^reader.html', views.reader_view),
    url(r'^reader.doaction=readerDel&ID=(\d+)', views.reader_delview),
    url(r'^reader.doaction=readerModifyQuery&ID=(\d+)', views.reader_upview),
    url(r'^readerup.html/(\d+)', views.readerupview),
    url(r'^readerType.html', views.readerType_view),
    url(r'^updateReaderType/ID=(\d+)', views.readerType_upview),
    url(r'^updateReaderType/readerTypeup.html/(\d+)', views.readerTypeupview),
    url(r'^readerType.doaction=readerTypeDel&ID=(\d+)', views.readerType_delview),
    url(r'^readerType_add.jsp', views.readerType_addview),
    url(r'^readerTypeadd.html', views.readerTypeaddview),
    url(r'^reader_add.jsp', views.reader_addview),
    url(r'^readeradd.html', views.readeraddview),



]