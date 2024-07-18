from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError


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

    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']
    #     if not all(char.isdigit() or char == '+' for char in phone):
    #         raise forms.ValidationError("Phone number can only contain digits and the plus sign.")
    #     return phone


