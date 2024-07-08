from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    
    """
    class Meta:
        model = Booking
        fields = (
            'user', 'car', 'first_name', 'last_name', 'date_of_birth',
            'start_date', 'end_date', 'pick_up_time', 'drop_off_time',
            'pickup_office', 'return_office', 'child_seat', 'child_seat_option',
            'extra_insurance', 'rules_agreement', 'status', 'total_price'
        )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Disable child_seat_option field initially
        self.fields['child_seat_option'].widget.attrs['disabled'] = True
        # Add onchange event to child_seat field
        self.fields['child_seat'].widget.attrs['onchange'] = 'toggleChildSeatOption(this)'

    class Media:
        js = ('js/booking_form.js',)  # Include the JavaScript file