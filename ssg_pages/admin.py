from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Team
from django.utils.html import format_html

# Register your models here.

@admin.register(Team)
class TeamAdmin(SummernoteModelAdmin):
    """
    Display options for admin panel related to blog posts

    **Context**

    ``list display``
        allows position, firstname, lastname and updated on for list display properties
    ``list filter``
        allowed list filters, position and updated on
    ``search fields``
        allowed search fields, position, first and last name
    ``summernote``
        allows summernote text editor on content field
    """
    
    # Thumbnail function, to display user image in admin panel
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.profile_image.url))
    thumbnail.short_description = 'Image'
    
    #Admin Panel Display and Filter Options
    list_display = ('position', 'thumbnail', 'first_name', 'last_name', 'updated_on')
    list_filter = ('position', 'updated_on')
    list_display_links = ('position','thumbnail', 'first_name', 'last_name',)
    search_fields = ('position', 'first_name', 'last_name',)
    summernote_fields = ('content')
    