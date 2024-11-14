"""
Admin configuration for the Game model.

This module sets up the admin interface for the Game model, including display options, filters, search fields, prepopulated fields, and integration with the Summernote text editor.

Classes:
    GamesAdmin(SummernoteModelAdmin): Custom admin interface for the Game model.

GamesAdmin:
    list_display:
        Specifies the fields to display in the list view: game title, thumbnail, slug, creator, game brief, and is featured.
    list_filter:
        Specifies the fields to filter the list view by: is featured.
    search_fields:
        Specifies the fields to include in the search functionality: game title, game brief, and description.
    list_display_links:
        Specifies the fields that should be clickable links in the list view: game title, thumbnail, and game brief.
    list_editable:
        Specifies the fields that should be editable directly in the list view: is featured.
    prepopulated_fields:
        Specifies the fields to prepopulate based on other fields: slug from game title.
    summernote_fields:
        Specifies the fields to use the Summernote text editor on: game brief and description.
"""

from django.contrib import admin  # Import Django admin
from django_summernote.admin import SummernoteModelAdmin  # Import SummernoteModelAdmin for rich text editing
from .models import Game  # Import the Game model
from django.utils.html import format_html  # Import format_html for HTML formatting

# Register your models here.

@admin.register(Game)
class GamesAdmin(SummernoteModelAdmin):
    """
    Admin panel configuration for the Game model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: game title, thumbnail, slug, creator, game brief, and is featured.
    - `list_filter`:
        Specifies the fields to filter the list view by: is featured.
    - `search_fields`:
        Specifies the fields to include in the search functionality: game title, game brief, and description.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view: game title, thumbnail, and game brief.
    - `list_editable`:
        Specifies the fields that should be editable directly in the list view: is featured.
    - `prepopulated_fields`:
        Specifies the fields to prepopulate based on other fields: slug from game title.
    - `summernote_fields`:
        Specifies the fields to use the Summernote text editor on: game brief and description.
    """
    
    def thumbnail(self, object):
        """
        Custom method to display the game's main image as a thumbnail in the admin list view.
        """
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.game_image_main.url))
    thumbnail.short_description = 'Image'
    
    list_display = ('game_title', 'thumbnail', 'slug','creator', 'game_brief', 'is_featured')  # Fields to display in the list view
    search_fields = ['game_title', 'game_brief', 'description']  # Fields to include in the search functionality
    list_display_links = ('game_title','thumbnail', 'game_brief',)  # Fields that should be clickable links in the list view
    list_filter = ('is_featured',)  # Fields to filter the list view by
    list_editable = ('is_featured',)  # Fields that should be editable directly in the list view
    prepopulated_fields = {'slug': ('game_title',)}  # Fields to prepopulate based on other fields
    summernote_fields = ('game_brief', 'description',)  # Fields to use the Summernote text editor on