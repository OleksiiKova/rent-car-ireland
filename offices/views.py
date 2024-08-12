from django.shortcuts import render
from django.views import generic
from .models import Office


# Create your views here.
class OfficeList(generic.ListView):
    """
    View that displays a list of all offices.

    This view uses the ListView generic class-based view to retrieve and
    display a list of Office objects. It renders the data using the
    'offices/office_list.html' template.

    Attributes:
        queryset (QuerySet): The queryset to retrieve Office objects. Defaults
                             to all Office objects.
        template_name (str): The name of the template to use for rendering the
                             view.
    """
    queryset = Office.objects.all().order_by('name')
    template_name = "offices/office_list.html"
