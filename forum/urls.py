from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('forum/', views.forum, name='forums'),
    path('forum/<int:entry_id>/', views.forum, name='forum'),
    path('api/forums/', views.api_forums, name='api_forums'),
    path('api/forums/<int:entry_id>/', views.api_forums, name='api_forum'),
    path('api/vote/', views.api_votes, name='api_votes'),
    path('api/vote/<int:entry_id>/', views.api_votes, name='api_vote')
]