from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pwd_Modify.html$', views.pwdModify_view),
]