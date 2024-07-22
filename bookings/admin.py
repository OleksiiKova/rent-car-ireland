from django.contrib import admin
from .models import Booking

# Register your models here.
admin.site.register(Booking)


class BookingAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Booking model.

    This class customizes the admin interface for the Booking model,
    specifying which fields to display in the list view and other
    administrative options.
    """
    list_display = ('user', 'car', 'start_date', 'end_date')
