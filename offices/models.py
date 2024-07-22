from django.db import models


# Create your models here.
class Office(models.Model):
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
        if self.latitude and self.longitude:
            return (
                    f'https://www.google.com/maps?q={self.latitude},'
                    f'{self.longitude}'
            )
        return None

    def __str__(self):
        return self.name
