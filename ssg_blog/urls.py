"""
URL configuration for the blog application.

This module defines the URL patterns for the blog application, mapping URLs to views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.Blog.as_view(), name='blog'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]
