from django.urls import path
from . import views
# from .views import home, BookingListView

urlpatterns = [
    path('', views.home, name='home'),
    # path('booking/', BookingListView.as_view(), name='booking'),
]