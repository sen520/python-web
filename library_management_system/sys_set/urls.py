from django.conf.urls import url

from sys_set import views

urlpatterns=[
    url(r'^library_modify.html', views.modify_view),
    url(r'^libraryModify', views.libraryModify_view),
    url(r'^main.html', views.main_view),
    url(r'^manager.html', views.manager_view),
    url(r'^manage.html', views.manage_view),
    url(r'^manager_add.jsp', views.add_view),
    url(r'^update/(\d+)', views.purview_view),
    url(r'^update/update.html/(\d+)', views.update_view),
    url(r'^del/(\d+)', views.del_view),
    url(r'^parameter_modify.html', views.pm_view),
    url(r'^parameterModify', views.parameter_view),
    url(r'^bookcase.html', views.bookcase_view),
    url(r'^bookcase_add.jsp', views.bookadd_view),
    url(r'^dell/(\d+)', views.dell_view),
    url(r'^update_book/updatebook.html/(\d+)', views.updet_view),
    url(r'^update_book/(\d+)', views.updete_view),
    url(r'^bookadd.html', views.bookad_view),
]