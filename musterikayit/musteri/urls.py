from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [


        url('index/', customer_index, name= 'index'),
        url(r'^(?P<id>\d+)/detail/$', customer_detail, name='detail'),
        url('create/', customer_create, name='create'),
        url(r'^(?P<id>\d+)/update/$',customer_update,name = 'update'),
        url(r'^(?P<id>\d+)/delete/$', customer_delete, name='delete'),

     
]
