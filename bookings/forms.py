from django import forms
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ValidationError
from .models import Booking
from offices.models import Office
from datetime import datetime, timedelta, date


def validate_phone_number(value):
    """
    Validates that the phone number starts with '+' and contains only
    digits after it.

    Args:
        value (str): The phone number to validate.

    Raises:
        ValidationError: If the phone number does not start with '+' or
        contains non-digit characters.
    """
    if not value[1:].isdigit() or not value.startswith('+'):
        raise ValidationError(
            'Phone number must start with "+" and '
            'contain only digits after it.'
        )


class BookingForm(forms.ModelForm):
    """
    A form for creating or updating booking instances.

    This form includes fields for the booking details and additional
    validation.
    """
    phone_number = forms.CharField(
        max_length=15,
        initial='+',
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={
            'type': 'tel',
        })
    )

    class Meta:
        model = Booking
        fields = (
            'pickup_office', 'return_office', 'start_date', 'pick_up_time',
            'end_date', 'drop_off_time', 'car', 'first_name', 'last_name',
            'email', 'phone_number', 'date_of_birth', 'child_seat',
            'child_seat_option', 'extra_insurance', 'rules_agreement',
            'total_price', 'rental_days'
        )
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.TextInput(
                attrs={'type': 'tel', 'pattern': '[0-9]+'}
                ),
        }

    def __init__(self, *args, **kwargs):
        """
        Initialize the form and set specific fields as read-only.

        Also configures the initial state of fields and their attributes.
        """
        super().__init__(*args, **kwargs)
        self._set_readonly_fields()
        self._disable_child_seat_option()
        self._add_onchange_event_to_child_seat()

    def _set_readonly_fields(self):
        """
        Sets specified fields as read-only by assigning them a CSS class.
        """
        readonly_fields = [
            'pickup_office', 'start_date', 'pick_up_time',
            'return_office', 'end_date', 'drop_off_time', 'car'
        ]
        for field in readonly_fields:
            self.fields[field].widget.attrs['class'] = (
                'form-control-plaintext '
                'hide-select-arrow'
            )

    def _disable_child_seat_option(self):
        """
        Disables the 'child_seat_option' field initially.
        """
        self.fields['child_seat_option'].widget.attrs['disabled'] = True

    def _add_onchange_event_to_child_seat(self):
        """
        Adds an 'onchange' event handler to the 'child_seat' field.
        """
        self.fields['child_seat'].widget.attrs['onchange'] = (
            'toggleChildSeatOption(this)'
        )

    def clean_date_of_birth(self):
        """
        Validates that the user's age is between 23 and 70.

        Returns:
            date: The cleaned date of birth.

        Raises:
            ValidationError: If the user's age is not within the valid range.
        """
        dob = self.cleaned_data['date_of_birth']
        today = date.today()
        age = today.year - dob.year - (
            (today.month, today.day) < (dob.month, dob.day)
            )

        if age < 23 or age > 70:
            self.add_error('date_of_birth', 'According to our rules, the age '
                           'must be between 23 and 70 years!')

        return dob


class SearchForm(forms.Form):
    """
    A form for searching bookings based on pickup and return offices, dates,
    and times.
    """
    pickup_office = forms.ModelChoiceField(
        queryset=Office.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    return_office = forms.ModelChoiceField(
        queryset=Office.objects.all(),
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    start_date = forms.DateField(
        label='Start Date', widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ))
    pick_up_time = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={'class': 'form-control'})
        )
    end_date = forms.DateField(
        label='End Date', widget=forms.DateInput(
            attrs={'type': 'date', 'class': 'form-control'}
        ))
    drop_off_time = forms.ChoiceField(
        choices=[], widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        """
        Initialize the form, setting default office locations and time choices.

        Sets minimum date values to the current date and populates time choices
        based on office hours.
        """
        super().__init__(*args, **kwargs)
        self._set_minimum_date_values()
        self._set_default_offices()
        self._set_time_choices()

    def _set_minimum_date_values(self):
        """
        Sets the minimum date values for 'start_date' and 'end_date' fields to
        the current date.
        """
        self.fields['start_date'].widget.attrs['min'] = timezone.now().date()
        self.fields['end_date'].widget.attrs['min'] = timezone.now().date()

    def _set_default_offices(self):
        """
        Sets default offices to Dublin Airport if it exists; otherwise, set to
        the first available office.
        """
        dublin_airport = Office.objects.filter(name='Dublin Airport').first()
        if dublin_airport:
            self.fields['pickup_office'].initial = dublin_airport.id
            self.fields['return_office'].initial = dublin_airport.id
        else:
            first_office = Office.objects.first()
            if first_office:
                self.fields['pickup_office'].initial = first_office.id
                self.fields['return_office'].initial = first_office.id

    def _set_time_choices(self):
        """
        Sets the choices for pick-up and drop-off times based on the selected office.
        """
        # Retrieve the initial office
        initial_office_id = self.fields['pickup_office'].initial
        selected_office = Office.objects.filter(id=initial_office_id).first()

        if selected_office:
            self.fields['pick_up_time'].choices = (
                self.generate_pick_up_time_choices(
                    selected_office.opening_time, selected_office.closing_time
                )
            )
            self.fields['drop_off_time'].choices = (
                self.generate_drop_off_time_choices()
            )
        else:
            # Handle the case where no valid office is found, if necessary
            self.fields['pick_up_time'].choices = []
            self.fields['drop_off_time'].choices = []

    def generate_pick_up_time_choices(
        self, opening_time=None, closing_time=None
    ):
        """
        Generates a list of time choices for pick-up times based on the
        office's opening and closing hours.

        Args:
            opening_time (datetime.time): The office's opening time.
            closing_time (datetime.time): The office's closing time.

        Returns:
            list: A list of tuples representing the time choices.
        """
        times = []
        if opening_time and closing_time:
            current_time = datetime.combine(datetime.today(), opening_time)
            end_time = datetime.combine(datetime.today(), closing_time)
            while current_time <= end_time:
                time_str = current_time.strftime('%H:%M')
                times.append((time_str, time_str))
                current_time += timedelta(hours=1)
        return times

    def generate_drop_off_time_choices(self):
        """
        Generates a list of time choices for drop-off times.

        Returns:
            list: A list of tuples representing the time choices.
        """
        times = []
        start_time = datetime.strptime('00:00', '%H:%M')
        end_time = datetime.strptime('23:00', '%H:%M')
        while start_time <= end_time:
            time_str = start_time.strftime('%H:%M')
            times.append((time_str, time_str))
            start_time += timedelta(hours=1)
        return times

    def clean(self):
        """
        Cleans the form data and validates the date and time fields.

        Checks that end date is not earlier than start date and that drop-off
        time
        is not earlier than pick-up time on the same day.

        Returns:
            dict: The cleaned data.
        """
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        pick_up_time = cleaned_data.get("pick_up_time")
        drop_off_time = cleaned_data.get("drop_off_time")
        pickup_office = cleaned_data.get("pickup_office")

        if start_date and end_date and pick_up_time and drop_off_time:
            if end_date < start_date:
                self.add_error(
                    'end_date', 'End date cannot be earlier than start date.'
                    )
            if start_date == end_date:
                pick_up_time_dt = datetime.strptime(
                    pick_up_time, '%H:%M').time()
                drop_off_time_dt = datetime.strptime(
                    drop_off_time, '%H:%M').time()

                if drop_off_time_dt <= pick_up_time_dt:
                    self.add_error(
                        'drop_off_time',
                        (
                            "Return time cannot be earlier than or equal to "
                            "pickup time on the same day."
                        )
                    )

        return cleaned_data
