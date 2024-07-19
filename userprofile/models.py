from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)