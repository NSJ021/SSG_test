from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Game
from django.utils.html import format_html

# Register your models here.

# Classes
@admin.register(Game)
class GamesAdmin(SummernoteModelAdmin):
    """
    Display options for admin panel related to games

    **Context**

    ``list display``
        allows Game title, thumbnail, creator, description, and if the game is featured for list display properties
    ``search fields``
        # allowed search fields, game title and description
     ``list filter``
        allowed list filters, if the game is featured.
    ``summernote``
        allows summernote text editor on description field
    """
    
    # Thumbnail function, to display user image in admin panel
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.game_image_main.url))
    thumbnail.short_description = 'Image'
    
    
    list_display = ('game_title', 'thumbnail','creator', 'game_brief', 'is_featured')
    search_fields = ['game_title', 'game_brief', 'description']
    list_filter = ('is_featured',)
    # prepopulated_fields = {'slug': ('game_title',)}
    summernote_fields = ('game_brief', 'description',)