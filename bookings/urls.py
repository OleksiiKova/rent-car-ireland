from django.urls import path
from . import views


urlpatterns = [
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('bookings/edit/<int:booking_id>/',
         views.edit_booking, name='edit_booking'),
    path('bookings/delete/<int:booking_id>/',
         views.delete_booking, name='delete_booking'),
    path('booking-form/<int:car_id>/',
         views.booking_form, name='booking_form'),
    path('booking_details/<int:booking_id>/',
         views.booking_details, name='booking_details'),
]
