from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path, include

from lock.views import turnOn,turnOff,foo

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'close_door/$', turnOn),
    url(r'open_door/$', turnOff),
]