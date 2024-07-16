from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('material', views.material, name='material'),
    path('material/<str:material_id>/', views.material, name="specific-material"),
    path('materials/upload/', views.subirMaterial, name='material_upload'),
]         

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)