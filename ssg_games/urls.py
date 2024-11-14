"""
URL configuration for the SSG games application.

This module defines the URL patterns for the games application, mapping URLs to views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Games.as_view(), name="games"),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
]
