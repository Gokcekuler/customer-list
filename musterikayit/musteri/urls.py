from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [

        
        url('index/', musteri_index, name= 'index'),
        url(r'^(?P<id>\d+)/detail/$', musteri_detail, name='detail'),
        url('create/', musteri_create, name='create'),
        url(r'^(?P<id>\d+)/update/$',musteri_update,name = 'update'),
        url(r'^(?P<id>\d+)/delete/$', musteri_delete, name='delete'),

        
]
