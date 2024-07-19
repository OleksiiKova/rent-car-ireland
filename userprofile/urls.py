from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile_view, name='my_profile'),
    path('leave_review/<int:booking_id>/', views.leave_review, name='leave_review'),
]