"""
Configuration for the SSG blog application.
"""
from django.apps import AppConfig

class SsgBlogConfig(AppConfig):
    """
    Configuration for the SSG blog application.

    Args:
        AppConfig (class): Configuration class for the Django application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ssg_blog'
