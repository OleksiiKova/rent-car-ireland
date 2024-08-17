from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Booking model.

    This class customizes the Django admin interface for the Booking model
    using Summernote for rich text editing. It specifies which fields to
    display in the list view, enables search functionality for the user field,
    and allows filtering by car and creation date.

    Attributes:
        list_display (tuple): Fields to display in the list view, including
                              the user, car, start date, end date, and
                              creation date.
        search_fields (list): Fields that can be searched, specifically the
                              user.
        list_filter (tuple): Fields by which the list can be filtered,
                              including car and creation date.
    """
    list_display = ('user', 'car', 'start_date', 'end_date', 'created_at')
    search_fields = ['user']
    list_filter = ('car', 'created_at')
