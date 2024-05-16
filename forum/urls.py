from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('foro', views.forum, name='foro'),
    path('foro/<int:forum_id>/', views.forum, name='foro_with_id'),  # URL with forum_id
]
