from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from star_ratings.models import Rating
from .models import UserProfile, Review, ContactMessage


def validate_phone_number(value):
    """
    Validates that the phone number starts with a '+' and contains only
    digits after it.

    Args:
        value (str): The phone number to validate.

    Raises:
        ValidationError: If the phone number does not start with '+' or
        contain only digits.
    """
    if not value[1:].isdigit() or not value.startswith('+'):
        raise ValidationError(
            'Phone number must start with "+" and '
            'contain only digits after it.'
        )


class UserProfileForm(forms.ModelForm):
    """
    A form for creating and updating UserProfile instances.

    This form allows users to enter their personal information,
    including phone number validation.
    The phone number field is optional and should start with a '+'
    followed by digits.

    Attributes:
        phone (CharField): A phone number field with validation to ensure
        it starts with '+' and contains only digits.
    """
    phone = forms.CharField(
        max_length=15,
        required=False,
        initial='+',
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={
            'type': 'tel',
        })
    )

    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'email', 'phone']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.TextInput(
                attrs={'type': 'tel', 'pattern': '[0-9]+'}
                ),
        }


class ReviewForm(forms.ModelForm):
    """
    A form for creating and submitting reviews.

    This form allows users to rate and comment on an entity.
    It includes options for anonymous submissions
    and uses radio buttons for rating selection.

    Attributes:
        rating (ChoiceField): A field for selecting a rating from 1 to 5 stars.
        is_anonymous (BooleanField): An optional field for submitting the
        review anonymously.
    """
    rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)],
                               widget=forms.RadioSelect(
                                attrs={'class': 'star-rating'}))
    is_anonymous = forms.BooleanField(
        required=False, initial=False, label='Leave anonymously')

    class Meta:
        model = Review
        fields = ['rating', 'comment', 'is_anonymous']


class ContactForm(forms.ModelForm):
    """
    A form for users to send a contact message.

    This form allows users to enter their name, email, and a message.
    It is used for contact or support requests.

    Attributes:
        name (CharField): A field for the user's name.
        email (EmailField): A field for the user's email address.
        message (CharField): A field for the user's message.
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class SignUpForm(forms.ModelForm):
    """
    A form for user registration.

    This class represents a form used to register a new user. It inherits from
    `forms.ModelForm` and includes additional fields for password and password
    confirmation. Validation checks if the passwords match.

    Fields:
    - username: The username of the user.
    - email: The user's email address (optional).
    - password1: The user's password.
    - password2: Password confirmation for verification.

    Methods:
    - clean_password2: Ensures that the password and its confirmation match.
    """
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(
        widget=forms.PasswordInput, label='Password (again)')

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'username'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),
        }

    def clean_password2(self):
        """
        Validates that the password and its confirmation match.

        Compares the values of 'password1' and 'password2'. If they do not
        match, a ValidationError is raised with an appropriate message.

        Returns:
            str: The confirmed password if validation is successful.

        Raises:
            ValidationError: If the passwords do not match.
        """
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
