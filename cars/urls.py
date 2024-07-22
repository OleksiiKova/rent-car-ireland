from django.urls import path
from . import views

urlpatterns = [
    path('', views.car_search, name='car_search'),
    path('update_pickup_time_choices/',
         views.update_pickup_time_choices, name='update_pickup_time_choices'),
    path('update_car_list/', views.update_car_list, name='update_car_list'),
]
