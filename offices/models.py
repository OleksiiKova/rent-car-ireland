from django.db import models


# Create your models here.
class Office(models.Model):
    """
    Represents an office location with contact details and operating hours.

    Attributes:
        name (str): The name of the office.
        phone_number (str): The phone number for the office.
        latitude (Decimal, optional): The latitude coordinate of the office
        location.
        longitude (Decimal, optional): The longitude coordinate of the office
        location.
        opening_time (Time): The opening time of the office.
        closing_time (Time): The closing time of the office.

    Methods:
        get_google_map_link: Generates a Google Maps link based on latitude
        and longitude.
    """
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=20, help_text='Office phone number')
    latitude = models.DecimalField(
        max_digits=30, decimal_places=20, blank=True, null=True,
        help_text='Latitude coordinate')
    longitude = models.DecimalField(
        max_digits=30, decimal_places=20, blank=True, null=True,
        help_text='Longitude coordinate')
    opening_time = models.TimeField(default='08:00')
    closing_time = models.TimeField(default='20:00')

    def get_google_map_link(self):
        """
        Generates a Google Maps link based on the office's latitude and
        longitude.

        If both latitude and longitude are available, this method constructs a
        Google Maps URL that displays the office location on the map. If the
        coordinates are not provided, it returns None.

        Returns:
            str or None: A Google Maps URL if latitude and longitude are
            provided, otherwise None.
        """
        if self.latitude and self.longitude:
            return (
                    f'https://www.google.com/maps?q={self.latitude},'
                    f'{self.longitude}'
            )
        return None

    def __str__(self):
        """
        Returns a string representation of the office.

        This method returns the name of the office.

        Returns:
            str: The name of the office.
        """
        return self.name
