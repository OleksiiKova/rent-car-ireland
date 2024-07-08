from django.db import models
from django.contrib.auth.models import User
from datetime import date
from cars.models import Car
from offices.models import Office

# Create your models here.
class Booking(models.Model):
    CHILD_SEAT_CHOICES = [
        ('0-9 kg', '0-9 kg'),
        ('9-18 kg', '9-18 kg'),
        ('booster', 'Booster'),
    ]

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('reviewed', 'Reviewed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=False, null=False)
    last_name = models.CharField(max_length=20, blank=False, null=False)
    date_of_birth = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    pick_up_time = models.TimeField()
    drop_off_time = models.TimeField()
    pickup_office = models.ForeignKey(Office, related_name='pickup_office', on_delete=models.CASCADE)
    return_office = models.ForeignKey(Office, related_name='return_office', on_delete=models.CASCADE)
    child_seat = models.BooleanField(default=False)
    child_seat_option = models.CharField(max_length=20, choices=CHILD_SEAT_CHOICES, blank=True, null=True)
    extra_insurance = models.BooleanField(default=False)
    rules_agreement = models.BooleanField(default=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"Booking for {self.user} - {self.car}"
