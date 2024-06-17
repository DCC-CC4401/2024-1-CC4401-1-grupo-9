from django.urls import path
from . import views

urlpatterns = [
    path('material', views.material, name='material'),
    path('material/<str:material_id>/', views.material, name="specific-material"),
    path('materials/upload/', views.subirMaterial, name='material_upload'),
]         
