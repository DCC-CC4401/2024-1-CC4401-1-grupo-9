from django.urls import path
from . import views

urlpatterns = [
    path('material', views.material, name='material'),
]         
