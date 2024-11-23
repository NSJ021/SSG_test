"""
URL configuration for the SSG pages application.

This module defines the URL patterns for the pages application, mapping URLs to views.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
]
