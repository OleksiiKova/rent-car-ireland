from django import forms
from .models import UserProfile, Review, ContactMessage
from django.core.exceptions import ValidationError
from star_ratings.models import Rating


def validate_phone_number(value):
    if not value[1:].isdigit() or not value.startswith('+'):
        raise ValidationError('Phone number must start with "+" and contain only digits after it.')


class UserProfileForm(forms.ModelForm):
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
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]+'}),
        }


class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=[(str(i), str(i)) for i in range(1, 6)],
                               widget=forms.RadioSelect(attrs={'class': 'star-rating'}))
    is_anonymous = forms.BooleanField(required=False, initial=False, label='Leave anonymously')

    class Meta:
        model = Review
        fields = ['rating', 'comment', 'is_anonymous']


class ContactForm(forms.ModelForm):
    """
    Form class for users to request a message
    """
    class Meta:
        model = ContactMessage
        fields = ('name', 'email', 'message',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)