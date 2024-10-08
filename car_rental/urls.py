"""
URL configuration for car_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from bookings import views
from cars import views
from userprofile import views as userprofile_views


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('contact/', userprofile_views.contact_us, name='contact_us'),
    path('my-profile/', include('userprofile.urls')),
    path("locations/", include("offices.urls"), name="office-urls"),
    path('summernote/', include('django_summernote.urls')),
    path('booking/', views.car_search, name='booking'),
    path('booking/', include('bookings.urls')),
    path('update_car_list/', views.update_car_list, name='update_car_list'),
    path('', userprofile_views.home, name='home'),
    path('update_pickup_time_choices/', views.update_pickup_time_choices,
         name='update_pickup_time_choices'),
]
