from django.shortcuts import render
from django.views import generic
from .models import Office

# Create your views here.
class OfficeList(generic.ListView):
    queryset = Office.objects.all()
    template_name = "office_list.html"