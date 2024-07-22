from django.apps import AppConfig


class BookingsConfig(AppConfig):
    """
    Django application configuration for the 'bookings' app.

    This class configures the 'bookings' application, specifying settings such
    as the default auto field type for models.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookings'
