from django.db import models
from django.contrib.auth.models import User
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
        ('MT', 'Manual Transmission'),
        ('AT', 'Automatic Transmission'),
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
    
