from django.apps import AppConfig


class CarsConfig(AppConfig):
    """
    Configuration for the 'cars' application.

    This class sets up the configuration for the 'cars' Django application.
    It specifies the default auto field type and the name of the application.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'
