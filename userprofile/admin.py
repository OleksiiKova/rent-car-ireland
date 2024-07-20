from django.contrib import admin
from .models import Review, ContactMessage

# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'rating', 'comment', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'comment')

admin.site.register(Review, ReviewAdmin)