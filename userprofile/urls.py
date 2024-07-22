from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_profile_view, name='my_profile'),
    path('leave_review/<int:booking_id>/',
         views.leave_review, name='leave_review'),
    path('userprofile/edit/<int:review_id>/',
         views.edit_review, name='edit_review'),
    path('my-reviews/', views.my_reviews, name='my_reviews'),
    path('userprofile/delete/<int:review_id>/',
         views.delete_review, name='delete_review'),
    path('all-reviews/', views.all_reviews, name='all_reviews'),
]
