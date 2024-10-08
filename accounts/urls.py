from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('forgot-password/', views.forgot_password_view, name='forgot'),
    path('profile/', views.profile, name='profile'),
    path('profile/<str:user_id>/', views.profile, name="another_profile"),
]