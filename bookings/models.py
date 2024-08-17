from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils import timezone
from cars.models import Car
from offices.models import Office


# Create your models here.
class Booking(models.Model):
    """
    Represents a car booking made by a user.

    **Attributes**

    ``user``
        The user who made the booking.
    ``car``
        The car being booked.
    ``first_name``
        The first name of the person making the booking.
    ``last_name``
        The last name of the person making the booking.
    ``phone_number``
        The phone number of the person making the booking.
    ``email``
        The email address of the person making the booking.
    ``date_of_birth``
        The date of birth of the person making the booking.
    ``start_date``
        The start date of the booking.
    ``end_date``
        The end date of the booking.
    ``pick_up_time``
        The time at which the car is to be picked up.
    ``drop_off_time``
        The time at which the car is to be returned.
    ``pickup_office``
        The office where the car will be picked up.
    ``return_office``
        The office where the car will be returned.
    ``child_seat``
        Whether a child seat is requested.
    ``child_seat_option``
        The type of child seat requested.
    ``extra_insurance``
        Whether extra insurance is requested.
    ``rules_agreement``
        Whether the booking rules have been agreed to.
    ``status``
        The status of the booking (e.g., confirmed, cancelled).
    ``total_price``
        The total price for the booking.
    ``rental_days``
        The number of days for which the car is rented.
    ``review_left``
        Whether a review has been left for the booking.
    ``created_at``
        The timestamp when the booking was created.

    **Meta**

    ``ordering``
        The default ordering of bookings by creation date (ascending).
    """
    CHILD_SEAT_CHOICES = [
        ('0-9 kg', 'Baby seat (0-9 kg)'),
        ('9-18 kg', 'Child seat (9-18 kg)'),
        ('booster', 'Booster seat (15-36 kg)'),
    ]

    STATUS_CHOICES = [
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
        ('reviewed', 'Reviewed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField()
    date_of_birth = models.DateField()
    start_date = models.DateField()
    end_date = models.DateField()
    pick_up_time = models.TimeField(blank=True, null=True)
    drop_off_time = models.TimeField(blank=True, null=True)
    pickup_office = models.ForeignKey(
        Office, related_name='pickup_office', on_delete=models.CASCADE
    )
    return_office = models.ForeignKey(
        Office, related_name='return_office', on_delete=models.CASCADE
    )
    child_seat = models.BooleanField(default=False)
    child_seat_option = models.CharField(
        max_length=20, choices=CHILD_SEAT_CHOICES, blank=True, null=True
    )
    extra_insurance = models.BooleanField(default=False)
    rules_agreement = models.BooleanField(default=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='confirmed'
    )
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )
    rental_days = models.IntegerField()
    review_left = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def can_leave_review(self):
        """
        Determines if a review can be left for the booking.

        A review can be left if the booking status is 'completed' and
        the end date of the booking is on or before today's date.

        Returns:
            bool: True if the booking status is 'completed' and
                  the end date is on or before today; otherwise, False.
        """
        return (
            self.status == 'completed' and
            self.end_date < timezone.now().date()
        )

    def __str__(self):
        """
        Returns a string representation of the booking.

        Returns:
            str: A string representing the booking, including user and car
            details.
        """
        return f"Booking for {self.user} - {self.car}"
