from django.db import models
from datetime import datetime
from cloudinary.models import CloudinaryField
import math


# Create your models here.
class Car(models.Model):
    """
    Car model representing a car available for rent.
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

    class Meta:
        ordering = ["make", "model"]

    def __str__(self):
        return f"{self.make} {self.model}"

    def calculate_total_cost(
        self, start_date, end_date, pick_up_time_str, drop_off_time_str,
        extra_insurance=None
    ):
        """
        Calculates the total rental cost and number of rental days for a given
        period.

        Args:
            start_date (date): The start date of the rental.
            end_date (date): The end date of the rental.
            pick_up_time_str (str): The pick-up time in 'HH:MM' format.
            drop_off_time_str (str): The drop-off time in 'HH:MM' format.
            extra_insurance (bool): Whether extra insurance is included.

        Returns:
            tuple: (number of rental days, total cost)
        """
        rental_hours = self._calculate_rental_hours(
            start_date, end_date, pick_up_time_str, drop_off_time_str)
        rental_days = self._calculate_rental_days(rental_hours)
        total_cost = self._calculate_base_cost(rental_days)
        total_cost = self._add_extra_insurance_cost(
            total_cost, rental_days, extra_insurance)

        return rental_days, round(total_cost, 2)

    def _calculate_rental_hours(
        self, start_date, end_date, pick_up_time_str, drop_off_time_str
    ):
        """
        Calculates the total rental period in hours.

        Args:
            start_date (date): The start date of the rental.
            end_date (date): The end date of the rental.
            pick_up_time_str (str): The pick-up time in 'HH:MM' format.
            drop_off_time_str (str): The drop-off time in 'HH:MM' format.

        Returns:
            float: Total rental period in hours.
        """
        pick_up_time = datetime.strptime(pick_up_time_str, "%H:%M").time()
        drop_off_time = datetime.strptime(drop_off_time_str, "%H:%M").time()

        start_datetime = datetime.combine(start_date, pick_up_time)
        end_datetime = datetime.combine(end_date, drop_off_time)

        return (end_datetime - start_datetime).total_seconds() / 3600

    def _calculate_rental_days(self, rental_hours):
        """
        Calculates the number of rental days, rounding up any fractional day.

        Args:
            rental_hours (float): Total rental period in hours.

        Returns:
            int: Number of rental days.
        """
        rental_days = math.ceil(rental_hours / 24)
        return max(rental_days, 1)

    def _calculate_base_cost(self, rental_days):
        """
        Calculates the base cost of the rental based on the number of days.

        Args:
            rental_days (int): Number of rental days.

        Returns:
            float: Base cost of the rental.
        """
        return rental_days * self.price_per_day

    def _add_extra_insurance_cost(
        self, total_cost, rental_days, extra_insurance
    ):
        """
        Adds extra insurance cost to the total rental cost if applicable.

        Args:
            total_cost (float): Current total cost of the rental.
            rental_days (int): Number of rental days.
            extra_insurance (bool): Whether extra insurance is included.

        Returns:
            float: Total cost including extra insurance if applicable.
        """
        if extra_insurance:
            total_cost += min(rental_days * 5, 50)
        return total_cost

    def calculate_car_rental_price(
        cars, start_date, end_date, pick_up_time, drop_off_time
    ):
        """
        Calculates rental prices for multiple cars.

        Args:
            cars (QuerySet): A queryset of Car objects.
            start_date (date): The start date of the rental.
            end_date (date): The end date of the rental.
            pick_up_time (str): The pick-up time in 'HH:MM' format.
            drop_off_time (str): The drop-off time in 'HH:MM' format.

        Returns:
            QuerySet: Updated queryset of Car objects with rental days and
            total costs.
        """
        for car in cars:
            rental_days, total_cost = car.calculate_total_cost(
                start_date, end_date, pick_up_time, drop_off_time)
            car.rental_days = rental_days
            car.total_cost = total_cost
        return cars

    def calculate_final_price(
        cars, start_date, end_date, pick_up_time, drop_off_time
    ):
        """
        Generates rental price information for multiple cars.

        Args:
            cars (QuerySet): A queryset of Car objects.
            start_date (date): The start date of the rental.
            end_date (date): The end date of the rental.
            pick_up_time (str): The pick-up time in 'HH:MM' format.
            drop_off_time (str): The drop-off time in 'HH:MM' format.

        Returns:
            list: A list of tuples containing Car objects and their respective
            rental days and total costs.
        """
        rental_info = []
        for car in cars:
            rental_days, total_cost = car.calculate_total_cost(
                start_date, end_date, pick_up_time, drop_off_time)
            rental_info.append((car, rental_days, total_cost))
        return rental_info
