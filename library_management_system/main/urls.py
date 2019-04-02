from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^main.html$', views.main_view),
]