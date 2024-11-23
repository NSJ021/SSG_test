"""
URL configuration for the SSG games application.

This module defines the URL patterns for the games application, mapping URLs to views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.games, name="games"),
    path('<slug:slug>/', views.game_detail, name='game_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
]
