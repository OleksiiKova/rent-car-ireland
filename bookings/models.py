from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils import timezone
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
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    pick_up_time = models.TimeField(blank=True, null=True)
    drop_off_time = models.TimeField(blank=True, null=True)
    pickup_office = models.ForeignKey(Office, related_name='pickup_office', on_delete=models.CASCADE)
    return_office = models.ForeignKey(Office, related_name='return_office', on_delete=models.CASCADE)
    child_seat = models.BooleanField(default=False)
    child_seat_option = models.CharField(max_length=20, choices=CHILD_SEAT_CHOICES, blank=True, null=True)
    extra_insurance = models.BooleanField(default=False)
    rules_agreement = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Booking for {self.user} - {self.car}"

    # def save(self, *args, **kwargs):
    #     if not self.rules_agreement:
    #         raise ValueError("You must agree to the rules before booking.")

    #     super().save(*args, **kwargs)

    # def clean(self):
    #     super().clean()
    #     if self.start_date and self.end_date and self.pick_up_time and self.drop_off_time:
    #         if self.end_date < self.start_date:
    #             self.add_error('end_date', 'End date cannot be earlier than start date.')
    #         if self.start_date == self.end_date:
    #             # pick_up_time_dt = datetime.strptime(pick_up_time, '%H:%M').time()
    #             # drop_off_time_dt = datetime.strptime(drop_off_time, '%H:%M').time()

    #             if drop_off_time_dt <= pick_up_time_dt:
    #                 self.add_error('drop_off_time', "Return time cannot be earlier than or equal to pickup time on the same day.")

        # if self.pick_up_time and self.drop_off_time:
        #     if self.drop_off_time <= self.pick_up_time:
        #         raise ValidationError('Drop off time must be later than pick up time.')

