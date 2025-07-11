from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin view for Contact Messages, configured for easy status updates.
    """
    list_display = ('subject', 'full_name', 'email', 'timestamp', 'is_read')
    list_editable = ('is_read',)
    list_display_links = ('subject',)
    list_filter = ('is_read', 'timestamp')
    search_fields = ('full_name', 'email', 'subject', 'message')
    readonly_fields = ('full_name', 'email', 'subject', 'message', 'timestamp')