from django.urls import path
from . import views


urlpatterns = [
    path('', views.OfficeList.as_view(), name='locations'),
]
