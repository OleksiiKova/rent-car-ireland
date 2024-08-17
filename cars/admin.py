from django.contrib import admin
from .models import Car


# Register your models here.
@admin.site.register(Car)
class CarAdmin(SummernoteModelAdmin):
    """
    Admin interface configuration for the Car model.

    This class customizes the Django admin interface for the Car model using
    Summernote for rich text editing. It specifies which fields to display in
    the list view, enables search functionality on specific fields, and allows
    filtering of the list by various attributes of the car.

    Attributes:
        list_display (tuple): Fields to display in the list view, including
                              make, model, type, transmission, and fuel type.
        search_fields (list): Fields that can be searched, specifically
                              make and model.
        list_filter (tuple): Fields by which the list can be filtered,
                              including make, model, type, transmission,
                              and fuel type.
    """
    list_display = ('make', 'model', 'type', 'transmission', 'fuel_type')
    search_fields = ['make', 'model']
    list_filter = ('make', 'model', 'type', 'transmission', 'fuel_type')
