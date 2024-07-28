from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from datetime import datetime, timedelta
from django.utils import timezone
from offices.models import Office
from .forms import BookingForm
from .views import (
    parse_date,
    get_office_by_id,
    get_user_profile_data,
    calc_rental_info,
    handle_post_request
)
from userprofile.test_data import create_test_data


class UtilityFunctionsTestCase(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating necessary test data including
        a user, car, office, booking, and review. This data is used in the
        form tests.
        """
        self.user, self.car, self.office, self.booking, self.review = (
            create_test_data()
        )

    def test_parse_date_valid(self):
        """
        Test the `parse_date` function with a valid date string.

        This test verifies that the `parse_date` function correctly parses a
        date string in the format "%d %B %Y" and returns a `datetime.date`
        object corresponding to the input date.
        """
        date_str = "27 July 2024"
        parsed_date = parse_date(date_str)
        expected_date = datetime.strptime(date_str, "%d %B %Y").date()
        self.assertEqual(parsed_date, expected_date)

    def test_parse_date_invalid(self):
        """
        Test the `parse_date` function with an invalid date string.

        This test verifies that the `parse_date` function raises a `ValueError`
        when given a date string that does not match the expected format.
        """
        with self.assertRaises(ValueError):
            parse_date("07-27-2024")

    def test_get_office_by_id_exists(self):
        """
        Test the `get_office_by_id` function when the office exists.

        This test verifies that the `get_office_by_id` function correctly
        fetches an `Office` object from the database using its ID.
        """
        office = Office.objects.create(name="Main Office")
        fetched_office = get_office_by_id(office.id)
        self.assertEqual(fetched_office, office)

    def test_get_office_by_id_does_not_exist(self):
        """
        Test the `get_office_by_id` function when the office does not exist.

        This test verifies that the `get_office_by_id` function returns `None`
        when an office with the given ID does not exist in the database.
        """
        fetched_office = get_office_by_id(999)
        self.assertIsNone(fetched_office)

    def test_calc_rental_info(self):
        """
        Test the `calc_rental_info` function with valid inputs.

        This test verifies that the `calc_rental_info` function calculates the
        rental days and total cost correctly based on the provided start and
        end dates, pick-up time, and drop-off time. It checks that the
        calculated values match the expected values based on the car's price
        per day.
        """
        start_date = datetime(2024, 7, 27, 10, 0)
        end_date = datetime(2024, 7, 30, 14, 0)
        pick_up_time = "10:00"
        drop_off_time = "14:00"

        rental_days, total_cost = calc_rental_info(
            self.car, start_date.date(), end_date.date(),
            pick_up_time, drop_off_time
        )
        start_datetime = datetime.combine(
            start_date.date(), datetime.strptime(pick_up_time, "%H:%M").time())
        end_datetime = datetime.combine(
            end_date.date(), datetime.strptime(drop_off_time, "%H:%M").time())
        if end_datetime < start_datetime:
            end_datetime += timedelta(days=1)

        days_diff = (
            end_datetime - start_datetime).total_seconds() / (24 * 3600)
        expected_rental_days = max(int(days_diff) + (days_diff % 1 > 0), 1)
        expected_total_cost = self.car.price_per_day * expected_rental_days

        self.assertEqual(rental_days, expected_rental_days)
        self.assertEqual(total_cost, expected_total_cost)


class BookingFormViewTest(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating necessary test data including
        a user, car, office, booking, and review. This data is used in the
        form tests.
        """
        self.user, self.car, self.office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

    def test_booking_form_rendering(self):
        """
        Test that the booking form is rendered correctly with the given GET
        parameters.

        This test verifies that the `booking_form` view returns a successful
        response (status code 200) and contains the form with the expected
        fields. It also ensures that the correct form is rendered in the
        context of the response.
        """
        response = self.client.get(
            reverse('booking_form', args=[self.car.id]), {
                'start_date': '29 July 2024',
                'end_date': '30 July 2024',
                'pick_up_time': '10:00',
                'drop_off_time': '12:00',
                'pickup_office': self.office.id,
                'return_office': self.office.id,
            })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Complete Your Booking')
        self.assertIsInstance(response.context['form'], BookingForm)
