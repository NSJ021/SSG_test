"""
URL configuration for the SSG Accounts application.

This module defines the URL patterns for the games application, mapping URLs to views.
"""

from django.urls import path
from . import views

urlpatterns = [

    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
]
