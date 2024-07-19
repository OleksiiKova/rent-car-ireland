from django.contrib import admin
from .models import Booking

# Register your models here.
admin.site.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('user', 'car', 'start_date', 'end_date')