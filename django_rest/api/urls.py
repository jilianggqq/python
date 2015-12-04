# from django.conf.urls import patterns, url

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello/$', views.hello_world, name='hello_world'),
    url(r'^tasks/$', views.task_list, name='task_list'),
    url(r'^tasks/(?P<pk>[0-9]+)$', views.task_detail, name='task_detail'),
]
