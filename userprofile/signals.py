from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Signal receiver that creates a UserProfile instance whenever a new User
    is created.

    This function is triggered after a User instance is saved. If the User
    instance was created
    (i.e., it's a new User), a corresponding UserProfile is created with
    default values.

    Args:
        sender (Model): The model class that sent the signal
        (User in this case).
        instance (User): The actual instance of the model being saved.
        created (bool): A boolean indicating whether a new record was created.
        **kwargs: Additional keyword arguments.
    """
    if created:
        UserProfile.objects.create(
            user=instance,
            email=instance.email,
            first_name='',
            last_name='',
            date_of_birth=None,
            phone=''
        )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Signal receiver that saves the UserProfile instance whenever the
    associated User is saved.

    This function is triggered after a User instance is saved. It ensures
    that the corresponding
    UserProfile instance is also saved.

    Args:
        sender (Model): The model class that sent the signal
        (User in this case).
        instance (User): The actual instance of the model being saved.
        **kwargs: Additional keyword arguments.
    """
    instance.userprofile.save()
