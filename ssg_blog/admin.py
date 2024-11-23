"""
Admin configuration for the Blog and Comment models.

This module sets up the admin interface for the Blog and Comment models, 
including display options, filters, search fields, prepopulated fields, 
and integration with the Summernote text editor.

Classes:
    BlogAdmin(SummernoteModelAdmin): Custom admin interface for the Blog model.
    CommentAdmin(SummernoteModelAdmin): Custom admin interface for the Comment model.

BlogAdmin:
    list_display:
        Specifies the fields to display in the list view: 
        title, thumbnail, slug, author, status, created on, and is featured.
    list_filter:
        Specifies the fields to filter the list view by: 
        status, created on, and author.
    search_fields:
        Specifies the fields to include in the search functionality: title and content.
    list_display_links:
        Specifies the fields that should be clickable links in the list view: 
        title, thumbnail, and author.
    list_editable:
        Specifies the fields that should be editable directly in the list view: is featured.
    prepopulated_fields:
        Specifies the fields to prepopulate based on other fields: slug from title.
    summernote_fields:
        Specifies the fields to use the Summernote text editor on: content.
    thumbnail:
        Custom method to display the blog's featured image as a thumbnail in the admin list view.

CommentAdmin:
    list_display:
        Specifies the fields to display in the list view: 
        post, body, author, approved, and created on.
    list_filter:
        Specifies the fields to filter the list view by: author, created on, and approved.
    search_fields:
        Specifies the fields to include in the search functionality: 
        post, body, author, and created on.
    list_display_links:
        Specifies the fields that should be clickable links in the list view:
        post, body, and author.
"""
from django.utils.html import format_html
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


# Admin configuration for the Post model
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin panel configuration for the Blog Post model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: 
        title, thumbnail, slug, author, status, created on, and is featured.
    - `list_filter`:
        Specifies the fields to filter the list view by: status, created on, and author.
    - `search_fields`:
        Specifies the fields to include in the search functionality: title and content.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view:
        title, thumbnail, and author.
    - `list_editable`:
        Specifies the fields that should be editable directly in the list view:
        status and is featured.
    - `prepopulated_fields`:
        Specifies the fields to prepopulate based on other fields: slug from title.
    - `summernote_fields`:
        Specifies the fields to use the Summernote text editor on: content.
    """
    # Custom method to display the blog's featured image as a thumbnail in the admin list view
    def thumbnail(self, blog):
        """
        Custom method to display the game's main image as a thumbnail in the admin list view.
        """
        return format_html(
            f'<img src="{blog.featured_image.url}" width="50" style="border-radius:50px;" />')
    thumbnail.short_description = 'Image'
    # Fields to display in the admin list view
    list_display = ('title', 'thumbnail', 'slug','author', 'status', 'created_on', 'is_featured')
    # Fields to include in the search functionality
    search_fields = ('title', 'content')
    # Fields that should be clickable links in the list view
    list_display_links = ('title','thumbnail', 'author',)
    # Fields that should be editable directly in the list view
    list_editable = ('status', 'is_featured',)
    # Fields to filter the list view by
    list_filter = ('status', 'created_on', 'author',)
    # Fields to prepopulate based on other fields
    prepopulated_fields = {'slug': ('title',)}
    # Fields to use the Summernote text editor on
    summernote_fields = ('content',)


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
        Specifies the fields to filter the list view by: author, created on, and approved.
    - `search_fields`:
        Specifies the fields to include in the search functionality:
        post, body, author, and created on.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view:
        post, body, and author.
    """
    # Fields to display in the admin list view
    list_display = ('post', 'body', 'author', 'approved', 'created_on')
    # Fields to filter the list view by
    list_filter = ('author', 'created_on', 'approved')
    # Fields that should be clickable links in the list view
    list_display_links = ('post','body', 'author',)
    # Fields that should be editable directly in the list view
    list_editable = ('approved',)
    # Fields to include in the search functionality
    search_fields = ('post', 'body', 'author', 'created_on')
