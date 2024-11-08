from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Team

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
    ``summernote``
        allows summernote text editor on content field
    """
    list_display = ('position', 'f_name', 'l_name', 'updated_on')
    list_filter = ('position', 'updated_on')
    summernote_fields = ('content')
    