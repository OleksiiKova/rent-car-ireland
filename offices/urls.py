from . import views
from django.urls import path


urlpatterns = [
    path('', views.OfficeList.as_view(), name='locations'),
]
