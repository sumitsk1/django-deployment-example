from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('relative/',views.relative, name='relative'),
    path('other/',views.other, name='other'),
  
]
