from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.booking_results, name='booking'),
    path('update_pickup_time_choices/', views.update_pickup_time_choices, name='update_pickup_time_choices'),
]