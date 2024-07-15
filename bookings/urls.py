from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('', views.booking_search, name='booking'),
    path('update_car_list/', views.update_car_list, name='update_car_list'),
    path('update_pickup_time_choices/', views.update_pickup_time_choices, name='update_pickup_time_choices'),
    path('booking-form/<int:car_id>/', views.booking_form, name='booking_form'),
    # path('booking/confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
]