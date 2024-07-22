from django.contrib import admin
from .models import Review, ContactMessage


# Register your models here.
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Admin view for managing ContactMessage model.

    This admin interface allows viewing and managing ContactMessage instances.
    It displays the 'message' and 'read' fields in the admin list view.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
    """
    list_display = ('message', 'read',)


class ReviewAdmin(admin.ModelAdmin):
    """
    Admin view for managing Review model.

    This admin interface allows viewing and managing Review instances.
    It displays the 'user', 'rating', 'comment', 'created_at', and 'approved'
    fields in the admin list view.
    It also provides filtering options based on 'approved' status and
    'created_at' date,
    and supports searching by 'user' username and 'comment' text.

    Attributes:
        list_display (tuple): Fields to display in the admin list view.
        list_filter (tuple): Filters to apply on the admin list view.
        search_fields (tuple): Fields to search for in the admin list view.
    """
    list_display = ('user', 'rating', 'comment', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('user__username', 'comment')


admin.site.register(Review, ReviewAdmin)
