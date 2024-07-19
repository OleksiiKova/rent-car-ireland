from django.contrib import admin
from .models import Review, ContactMessage

# Register your models here.
admin.site.register(Review)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)