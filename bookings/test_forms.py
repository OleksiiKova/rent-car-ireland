from django.test import TestCase
from django import forms
from django.utils import timezone
from datetime import datetime, timedelta
from .models import Booking, Office, Car
from offices.models import Office
from cars.models import Car
from .forms import BookingForm, SearchForm
from userprofile.test_data import create_test_data


class BookingFormTests(TestCase):
    """
    Tests for the BookingForm, ensuring that the form validates correctly
    for various scenarios including valid and invalid inputs.
    """
    def setUp(self):
        """
        Set up the test environment by creating necessary test data including
        a user, car, office, booking, and review. This data is used in the
        form tests.
        """
        self.user, self.car, self.office, self.booking, self.review = (
            create_test_data()
        )

    def test_valid_booking_form(self):
        """
        Test case for validating a BookingForm with all correct inputs. Ensures
        that the form is valid when all required fields are correctly provided.
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date(),
            'pick_up_time': '10:00',
            'end_date': timezone.now().date() + timedelta(days=7),
            'drop_off_time': '11:00',
            'car': self.car.id,
            'first_name': 'Mike',
            'last_name': 'Buf',
            'email': 'test@example.com',
            'phone_number': '+1234567890',
            'date_of_birth': timezone.now().date() - timedelta(days=365 * 30),
            'child_seat': True,
            'child_seat_option': '0-9 kg',
            'extra_insurance': True,
            'rules_agreement': True,
            'total_price': 299.99,
            'rental_days': 7,
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_phone_number(self):
        """
        Test case for an invalid phone number in the BookingForm. Ensures
        that the form is invalid and shows an error when the phone number
        does not start with a '+' sign.
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date(),
            'pick_up_time': '10:00',
            'end_date': timezone.now().date() + timedelta(days=7),
            'drop_off_time': '11:00',
            'car': self.car.id,
            'first_name': 'Mike',
            'last_name': 'Buf',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'date_of_birth': timezone.now().date() - timedelta(days=365 * 30),
            'child_seat': True,
            'child_seat_option': 'Front',
            'extra_insurance': True,
            'rules_agreement': True,
            'total_price': 299.99,
            'rental_days': 7,
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors)

    def test_age_validation(self):
        """
        Test case for validating the age of the user in the BookingForm.
        Ensures that the form is invalid and shows an error if the user's
        age is outside the acceptable range (23 to 70 years).
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date(),
            'pick_up_time': '10:00',
            'end_date': timezone.now().date() + timedelta(days=7),
            'drop_off_time': '11:00',
            'car': self.car.id,
            'first_name': 'Mike',
            'last_name': 'Buf',
            'email': 'test@example.com',
            'phone_number': '+1234567890',
            'date_of_birth': timezone.now().date() - timedelta(days=365 * 19),
            'child_seat': True,
            'child_seat_option': 'Front',
            'extra_insurance': True,
            'rules_agreement': True,
            'total_price': 299.99,
            'rental_days': 7,
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)


class SearchFormTests(TestCase):
    """
    Tests for the SearchForm, ensuring that the form validates correctly
    for various scenarios including valid and invalid inputs.
    """

    def setUp(self):
        """
        Set up the test environment by creating necessary test data including
        a user, car, office, booking, and review. This data is used in the
        form tests.
        """
        self.user, self.car, self.office, self.booking, self.review = (
            create_test_data()
        )

    def _create_search_form(self, data=None):
        """
        Create an instance of TestSearchForm with predefined time choices.

        Args:
            data (dict, optional): Data to initialize the form with.

        Returns:
            TestSearchForm: An instance of the customized SearchForm.
        """
        class TestSearchForm(SearchForm):
            def _set_time_choices(self):
                self.fields['pick_up_time'].choices = [
                    ('09:00', '09:00'),
                    ('10:00', '10:00'),
                    ('11:00', '11:00'),
                ]
                self.fields['drop_off_time'].choices = [
                    ('09:00', '09:00'),
                    ('10:00', '10:00'),
                    ('11:00', '11:00'),
                ]
        return TestSearchForm(data=data)

    def test_valid_search_form(self):
        """
        Test case for validating a SearchForm with correct inputs. Ensures
        that the form is valid when all required fields are correctly provided.
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date(),
            'pick_up_time': '10:00',
            'end_date': timezone.now().date() + timedelta(days=7),
            'drop_off_time': '11:00',
        }
        form = self._create_search_form(data=form_data)
        self.assertTrue(form.is_valid())

    def test_end_date_before_start_date(self):
        """
        Test case for an end date that is before the start date in the
        SearchForm.
        Ensures that the form is invalid and shows an error when the end date
        is earlier than the start date.
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date() + timedelta(days=7),
            'pick_up_time': '10:00',
            'end_date': timezone.now().date(),
            'drop_off_time': '11:00',
        }
        form = self._create_search_form(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('end_date', form.errors)

    def test_drop_off_time_before_pick_up_time(self):
        """
        Test case for a drop-off time that is before the pick-up time on the
        same day in the SearchForm. Ensures that the form is invalid and shows
        an error when the drop-off time is earlier than the pick-up time on
        the same day.
        """
        form_data = {
            'pickup_office': self.office.id,
            'return_office': self.office.id,
            'start_date': timezone.now().date(),
            'pick_up_time': '11:00',
            'end_date': timezone.now().date(),
            'drop_off_time': '10:00',
        }
        form = self._create_search_form(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('drop_off_time', form.errors)
