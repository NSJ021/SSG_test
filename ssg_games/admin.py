"""
Admin configuration for the Game model.

This module sets up the admin interface for the Game model, 
including display options, filters, search fields, prepopulated fields, 
and integration with the Summernote text editor.

Classes:
    GamesAdmin(SummernoteModelAdmin): Custom admin interface for the Game model.

GamesAdmin:
    list_display:
        Specifies the fields to display in the list view: game title, 
        thumbnail, slug, creator, game brief, and is featured.
    list_filter:
        Specifies the fields to filter the list view by: is featured.
    search_fields:
        Specifies the fields to include in the search functionality: 
        game title, game brief, and description.
    list_display_links:
        Specifies the fields that should be clickable links in the list view:
        game title, thumbnail, and game brief.
    list_editable:
        Specifies the fields that should be editable directly in the list view: is featured.
    prepopulated_fields:
        Specifies the fields to prepopulate based on other fields: slug from game title.
    summernote_fields:
        Specifies the fields to use the Summernote text editor on: game brief and description.
"""

from django.utils.html import format_html
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game, Comment

# Register your models here.

@admin.register(Game)
class GamesAdmin(SummernoteModelAdmin):
    """
    Admin panel configuration for the Game model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: game title, 
        thumbnail, slug, creator, game brief, and is featured.
    - `list_filter`:
        Specifies the fields to filter the list view by: is featured.
    - `search_fields`:
        Specifies the fields to include in the search functionality: 
        game title, game brief, and description.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view: game title, 
        thumbnail, and game brief.
    - `list_editable`:
        Specifies the fields that should be editable directly in the list view: is featured.
    - `prepopulated_fields`:
        Specifies the fields to prepopulate based on other fields: slug from game title.
    - `summernote_fields`:
        Specifies the fields to use the Summernote text editor on: game brief and description.
    """
    def game_thumbnail(self, game):
        """
        Custom method to display the game's main image as a thumbnail in the admin list view.
        """
        return format_html(
            f'<img src="{game.game_image_main.url}" width="50" style="border-radius:50px;" />')
    game_thumbnail.short_description = 'Image'
    # Fields to display in the admin list view
    list_display = ('game_title', 'game_thumbnail', 'slug','creator', 'game_brief', 'is_featured')
    search_fields = ['game_title', 'game_brief', 'description']
    list_display_links = ('game_title','game_thumbnail', 'game_brief',)
    list_filter = ('is_featured',)
    list_editable = ('is_featured',)
    prepopulated_fields = {'slug': ('game_title',)}
    summernote_fields = ('game_brief', 'description',)
    # Admin configuration for the Comment model
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Admin panel configuration for the Comment model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: 
        post, body, author, approved, and created on.
    - `list_filter`:
        Specifies the fields to filter the list view by: author, 
        created on, and approved.
    - `search_fields`:
        Specifies the fields to include in the search functionality: 
        post, body, author, and created on.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view: 
        post, body, and author.
    """
    # Fields to display in the admin list view
    list_display = ('game', 'body', 'author', 'approved', 'created_on')
    # Fields to filter the list view by
    list_filter = ('author', 'created_on', 'approved')
    # Fields that should be clickable links in the list view
    list_display_links = ('game','body', 'author',)
    # Fields that should be editable directly in the list view
    list_editable = ('approved',)
    # Fields to include in the search functionality
    search_fields = ('game', 'body', 'author', 'created_on')
