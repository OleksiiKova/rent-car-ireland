from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField

# Create your models here.
class Car(models.Model):
    """
    Car model to be able to create many Cars in Django's admin panel
    """

    TYPE_CHOICES = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('Cabriolet', 'Cabriolet'),
        ('Hatchback', 'Hatchback'),
        ('Station Wagon', 'Station Wagon'),
        ('Minivan', 'Minivan'),
        ('SUV', 'SUV'),
        ('Pickup Truck', 'Pickup Truck'),
    ]
    FUEL_CHOICES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric')
    ]
    TRANSMISSION_CHOICES = [
        ('MT', 'Manual'),
        ('AT', 'Automatic'),
    ]

    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    type = models.CharField(max_length=15, choices=TYPE_CHOICES)
    year = models.IntegerField()
    seats = models.IntegerField()
    doors = models.IntegerField()
    fuel_type = models.CharField(max_length=8, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=2, choices=TRANSMISSION_CHOICES)
    air_conditioning = models.BooleanField(default=True)
    navigation = models.BooleanField(default=True)
    availability = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def calculate_total_cost(self, start_date, end_date, pick_up_time_str, drop_off_time_str):
        # Convert time strings to time objects
        pick_up_time = datetime.strptime(pick_up_time_str, "%H:%M").time()
        drop_off_time = datetime.strptime(drop_off_time_str, "%H:%M").time()

        start_datetime = datetime.combine(start_date, pick_up_time)
        end_datetime = datetime.combine(end_date, drop_off_time)
        rental_days = (end_datetime - start_datetime).days

        # Ensure minimum rental period is one day
        if rental_days < 1:
            rental_days = 1
        return rental_days * self.price_per_day
    
