from django.contrib import admin
from .models import Office
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(Office)
class OfficeAdmin(SummernoteModelAdmin):

    list_display = ('name', 'phone_number')
    search_fields = ['name']
    list_filter = ('name',)
