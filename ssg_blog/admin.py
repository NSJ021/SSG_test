from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment
from django.utils.html import format_html

# Classes
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Display options for admin panel related to blog posts

    **Context**

    ``list display``
        allows title, slug status and created on for list display properties
    ``search fields``
        allowed search fields, title and content
     ``list filter``
        allowed list filters, status, created on and author
    ``prepopulated``
        prepopulated fields, sluig and title
    ``summernote``
        allows summernote text editor on content field
    """
    
    # Thumbnail function, to display user image in admin panel
    def thumbnail(self, object):
        return format_html('<img src="{}" width="50" style="border-radius:50px;" />'.format(object.featured_image.url))
    thumbnail.short_description = 'Image'
    
    
    list_display = ('title', 'thumbnail', 'slug','author', 'status', 'created_on',)
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on', 'author',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """
    Display options for admin panel related to blog comments

    **Context**

    ``list display``
        allows post, author, approved and created=on for list display properties
     ``list filter``
        allowed list filters, author, created-on and approved

    """
    list_display = ('post', 'body', 'author', 'approved', 'created_on')
    list_filter = ('author', 'created_on', 'approved')
    