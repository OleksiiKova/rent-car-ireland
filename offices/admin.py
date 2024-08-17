from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Office


# Register your models here.
@admin.register(Office)
class OfficeAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Office model.

    This class customizes the Django admin interface for the Office model by
    using Summernote for rich text editing. It specifies which fields to
    display in the list view, provides search functionality, and allows
    filtering of the list by office name.

    Attributes:
        list_display (tuple): Specifies the fields to display in the list view.
        search_fields (list): Defines the fields that can be searched.
        list_filter (tuple): Determines the fields by which the list can be
        filtered.
    """
    list_display = ('name', 'phone_number')
    search_fields = ['name']
    list_filter = ('name',)
