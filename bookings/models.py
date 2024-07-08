from django.db import models
from django.contrib.auth.models import User
from datetime import date
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
    date_of_birth = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    pick_up_time = models.TimeField(choices=[], blank=True, null=True)
    drop_off_time = models.TimeField(choices=[], blank=True, null=True)
    pickup_office = models.ForeignKey(Office, related_name='pickup_office', on_delete=models.CASCADE)
    return_office = models.ForeignKey(Office, related_name='return_office', on_delete=models.CASCADE)
    child_seat = models.BooleanField(default=False)
    child_seat_option = models.CharField(max_length=20, choices=CHILD_SEAT_CHOICES, blank=True, null=True)
    extra_insurance = models.BooleanField(default=False)
    rules_agreement = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='confirmed')
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )

    def __str__(self):
        return f"Booking for {self.user} - {self.car}"

    def save(self, *args, **kwargs):
        # Check that the user has checked the box to agree to the rules
        if not self.rules_agreement:
            raise ValueError("You must agree to the rules before booking.")

        if self.pickup_office_id:
            # Get the working hours of the pick-up office where user book a car
            office = self.pickup_office
            if office:
                opening_time = office.opening_time
                closing_time = office.closing_time

                # Create a list of available car pick-up times
                current_time = datetime.combine(self.start_date, opening_time)
                pickup_times = []
                while current_time <= datetime.combine(self.start_date, closing_time):
                    pickup_times.append((current_time.time(), current_time.strftime('%H:%M')))
                    current_time += timedelta(hours=1)

                # Update choices for the pick_up_time field
                self.pick_up_time = models.TimeField(choices=pickup_times, blank=True, null=True)

        # Create a list for the drop_off_time field from 00:00 to 23:00
        drop_off_times = []
        current_time = datetime.combine(self.start_date, datetime.min.time())
        while current_time <= datetime.combine(self.end_date, datetime.max.time()):
            drop_off_times.append((current_time.time(), current_time.strftime('%H:%M')))
            current_time += timedelta(hours=1)

        # Update choices for the drop_off_time field
        self.drop_off_time = models.TimeField(choices=drop_off_times, blank=True, null=True)

        super().save(*args, **kwargs)

    def clean(self):
        super().clean()

        # Check, that drop_off_time later than pick_up_time
        if self.pick_up_time and self.drop_off_time:
            if self.drop_off_time <= self.pick_up_time:
                raise ValidationError('Drop off time must be later than pick up time.')
            
