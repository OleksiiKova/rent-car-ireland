from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin configuration for the Booking model.

    This class customizes the admin interface for the Booking model,
    specifying which fields to display in the list view and other
    administrative options.
    """
    list_display = ('user', 'start_date', 'end_date')
    search_fields = ['car']
    list_filter = ('car',)