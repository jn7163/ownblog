#encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin
from . import views 


urlpatterns = [
    url(r'^getpassages', views.getpassages,name='getpassages'),
]