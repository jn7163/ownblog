#encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from . import views 


urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^passages/(?P<page>[0-9]+)$',views.passages,name='passages'),
    url(r'^(?P<pid>[0-9]+)$',views.passage1,name='passage'),
    url(r'^(?P<pid>[0-9]+)/(?P<commentpage>[0-9]+)$',views.passage,name='passage'),
    url(r'^about$',views.about,name='about'),
    url(r'^add$',views.add,name='add'),
    url(r'^change/(?P<pid>[0-9]+)$',views.change,name='change')
]