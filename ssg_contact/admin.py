"""
Admin panel configuration for the Contact model.
"""
from django.contrib import admin
from .models import UserMessage

# Register your models here.
@admin.register(UserMessage)
class ContactAdmin(admin.ModelAdmin):
    """
    Admin panel configuration for the Contact model.

    **Attributes:**

    - `list_display`:
        Specifies the fields to display in the list view: name, 
        email, subject, phone number, and created on.
    - `list_filter`:
        Specifies the fields to filter the list view by: created on.
    - `search_fields`:
        Specifies the fields to include in the search functionality: name, email, and subject.
    - `list_display_links`:
        Specifies the fields that should be clickable links in the list view:
        name, email, and subject.
    """
    list_display = ('user','name', 'email', 'subject',
                    'phone_number', 'created_on', 'message_read', 'message_replied')
    list_filter = ('email','created_on', 'message_read', 'message_replied')
    search_fields = ('name', 'email', 'subject')
    list_display_links = ('user','name', 'email', 'subject')
    list_editable = ('message_read', 'message_replied')
    list_editable = ('message_read', 'message_replied')
