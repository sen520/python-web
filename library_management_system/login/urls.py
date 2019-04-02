from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login.html$', views.login_view),
    url(r'^login$', views.login_view),
    url(r'^$', views.login_view),
]