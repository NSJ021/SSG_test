"""
This file is used to define URL patterns for ssg_contact app
"""
from django.urls import path
from . import views

urlpatterns = [

    path('contact', views.user_contact, name='contact'),

]