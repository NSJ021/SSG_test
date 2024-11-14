"""
Admin configuration for the Team model.

This module sets up the admin interface for the Team model, including display options, filters, search fields, and integration with the Summernote text editor.

Classes:
    TeamAdmin(SummernoteModelAdmin): Custom admin interface for the Team model.
"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Team
from django.utils.html import format_html

# Register your models here.

@admin.register(Team)
class TeamAdmin(SummernoteModelAdmin):
    """
    Admin panel configuration for the Team model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: position, thumbnail, first name, last name, and updated on.
    - `list_filter`:
        Specifies the fields to filter the list view by: position and updated on.
    - `search_fields`:
        Specifies the fields to include in the search functionality: position, first name, and last name.
    - `summernote_fields`:
        Specifies the fields to use the Summernote text editor on: content.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view: position, thumbnail, first name, and last name.
    """
    # Thumbnail function, to display user image in admin panel
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.profile_image.url))
    thumbnail.short_description = 'Image'
    
    # Admin Panel Display and Filter Options
    list_display = ('position', 'thumbnail', 'first_name', 'last_name', 'updated_on')
    list_filter = ('position', 'updated_on')
    list_display_links = ('position','thumbnail', 'first_name', 'last_name',)
    search_fields = ('position', 'first_name', 'last_name',)
    summernote_fields = ('content')
