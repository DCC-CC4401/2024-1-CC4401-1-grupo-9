from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('foro', views.forum, name='foro'),
]