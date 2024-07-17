from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Booking
from offices.models import Office
from datetime import datetime, timedelta


def validate_phone_number(value):
    if not value[1:].isdigit() or not value.startswith('+'):
        raise ValidationError('Phone number must start with "+" and contain only digits after it.')


class BookingForm(forms.ModelForm):
    """
    
    """
    phone_number = forms.CharField(
        max_length=15,
        initial='+',
        validators=[validate_phone_number],
        widget=forms.TextInput(attrs={
            'type': 'tel',
            'placeholder': 'Enter phone number'
        })
    )
    class Meta:
        model = Booking
        fields = (
            'pickup_office', 'return_office', 'start_date', 'pick_up_time', 'end_date', 'drop_off_time',
            'car', 'first_name', 'last_name', 'email', 'phone_number', 'date_of_birth',
            'child_seat', 'child_seat_option',
            'extra_insurance', 'rules_agreement', 'total_price', 'rental_days'
        )
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone_number': forms.TextInput(attrs={'type': 'tel', 'pattern': '[0-9]+'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set the specified fields as read-only
        readonly_fields = ['pickup_office', 'start_date', 'pick_up_time', 'return_office', 'end_date', 'drop_off_time', 'car']
        for field in readonly_fields:
            self.fields[field].widget.attrs['class'] = 'form-control-plaintext hide-select-arrow'

        # Disable child_seat_option field initially
        self.fields['child_seat_option'].widget.attrs['disabled'] = True
        # Add onchange event to child_seat field
        self.fields['child_seat'].widget.attrs['onchange'] = 'toggleChildSeatOption(this)'

    class Media:
        js = ('js/booking_form.js',)


class SearchForm(forms.Form):
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
    start_date = forms.DateField(label='Start Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    pick_up_time = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    end_date = forms.DateField(label='End Date', widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    drop_off_time = forms.ChoiceField(choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['start_date'].widget.attrs['min'] = timezone.now().date()
        self.fields['end_date'].widget.attrs['min'] = timezone.now().date()
        
        # Set default offices to Dublin Airport if it exists
        dublin_airport = Office.objects.filter(name='Dublin Airport').first()
        if dublin_airport:
            self.fields['pickup_office'].initial = dublin_airport.id
            self.fields['return_office'].initial = dublin_airport.id
        
        self.fields['pick_up_time'].choices = self.generate_pick_up_time_choices(dublin_airport.opening_time, dublin_airport.closing_time) if dublin_airport else []
        self.fields['drop_off_time'].choices = self.generate_drop_off_time_choices()

    def generate_pick_up_time_choices(self, opening_time=None, closing_time=None):
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
        times = []
        start_time = datetime.strptime('00:00', '%H:%M')
        end_time = datetime.strptime('23:00', '%H:%M')
        while start_time <= end_time:
            time_str = start_time.strftime('%H:%M')
            times.append((time_str, time_str))
            start_time += timedelta(hours=1)
        return times

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        pick_up_time = cleaned_data.get("pick_up_time")
        drop_off_time = cleaned_data.get("drop_off_time")
        pickup_office = cleaned_data.get("pickup_office")

        if start_date and end_date and pick_up_time and drop_off_time:
            if end_date < start_date:
                self.add_error('end_date', 'End date cannot be earlier than start date.')
            if start_date == end_date:
                pick_up_time_dt = datetime.strptime(pick_up_time, '%H:%M').time()
                drop_off_time_dt = datetime.strptime(drop_off_time, '%H:%M').time()

                if drop_off_time_dt <= pick_up_time_dt:
                    self.add_error('drop_off_time', "Return time cannot be earlier than or equal to pickup time on the same day.")

        return cleaned_data

    # def update_pick_up_time_choices(self, opening_time, closing_time):
    #     self.fields['pick_up_time'].choices = self.generate_pick_up_time_choices(opening_time, closing_time)

    # def update_drop_off_time_choices(self):
    #     self.fields['drop_off_time'].choices = self.generate_drop_off_time_choices()
        