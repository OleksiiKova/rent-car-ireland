from django.urls import path
from . import views


urlpatterns = [
    path('', views.booking_search, name='booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/edit/<int:booking_id>/', views.edit_booking, name='edit_booking'),
    path('bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('update_car_list/', views.update_car_list, name='update_car_list'),
    path('update_pickup_time_choices/', views.update_pickup_time_choices, name='update_pickup_time_choices'),
    path('booking-form/<int:car_id>/', views.booking_form, name='booking_form'),
    
]