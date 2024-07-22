from django.db import models
from django.contrib.auth.models import User
from bookings.models import Booking
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class UserProfile(models.Model):
    """
    Profile model for extending the default User model.

    This model allows users to have additional personal information such as
    first name, last name, date of birth, email, and phone number.

    Attributes:
        user (OneToOneField): A one-to-one relationship
        with Django's User model.
        first_name (CharField): The user's first name, which can be blank.
        last_name (CharField): The user's last name, which can be blank.
        date_of_birth (DateField): The user's date of birth,
        which can be null or blank.
        email (EmailField): The user's email address, which can be blank.
        phone (CharField): The user's phone number, which can be blank.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'


class Review(models.Model):
    """
    Model for storing user reviews related to bookings.

    This model captures the rating and comments provided by users for a
    specific booking. It includes fields for rating, comment, and metadata
    such as the creation date and approval status.

    Attributes:
        booking (OneToOneField): A one-to-one relationship with
        the Booking model.
        user (ForeignKey): A foreign key relationship with Django's User model.
        rating (IntegerField): The rating given by the user,
        ranging from 1 to 5.
        comment (TextField): The review comment provided by the user.
        created_at (DateTimeField): Timestamp for when the review was created.
        is_anonymous (BooleanField): Indicates whether the review is
        submitted anonymously.
        approved (BooleanField): Indicates whether the review has been
        approved for display.
    """
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    is_anonymous = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Review {self.comment} by {self.user}"


class ContactMessage(models.Model):
    """
    Model for storing contact messages from users.

    This model captures messages sent by users, including their name,
    email, and the message content. It also includes a flag to indicate
    whether the message has been read.

    Attributes:
        name (CharField): The name of the person sending the message.
        email (EmailField): The email address of the person sending
        the message.
        message (TextField): The content of the message.
        read (BooleanField): Indicates whether the message has been read.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message from {self.name}"
