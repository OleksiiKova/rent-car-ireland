from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone
from datetime import datetime, time, timedelta
from .models import Car
from userprofile.test_data import create_test_data
from bookings.forms import SearchForm


class CarViewTests(TestCase):
    def setUp(self):
        """
        Create necessary test data and log in for the test cases.
        """
        self.user, self.car, self.office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

        # Update the URL names to match those defined in urls.py
        self.car_search_url = reverse('booking')
        self.update_pickup_time_choices_url = reverse(
            'update_pickup_time_choices')
        self.update_car_list_url = reverse('update_car_list')

    def test_car_search_view_get(self):
        """
        Test that the car search view returns the correct response for 
        GET requests.
        """
        response = self.client.get(self.car_search_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/booking.html')
        self.assertIn('form', response.context)
        form = response.context['form']
        self.assertIn('drop_off_time', form.fields)
        self.assertIn('09:00', [choice[0] for choice in form.fields[
            'drop_off_time'].choices])
