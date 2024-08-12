from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Office


class OfficeListViewTest(TestCase):
    """
    Tests for the OfficeList view.
    """

    def setUp(self):
        """
        Set up test client and create sample Office objects.
        """
        self.client = Client()
        self.office_list_url = reverse('locations')

        self.office1 = Office.objects.create(
            name="Headquarters",
            phone_number="123-456-7890",
            latitude="40.712776",
            longitude="-74.005974",
            opening_time="09:00",
            closing_time="17:00"
        )
        self.office2 = Office.objects.create(
            name="Branch Office",
            phone_number="987-654-3210",
            latitude="34.052235",
            longitude="-118.243683",
            opening_time="10:00",
            closing_time="18:00"
        )

    def test_office_list_view_status_code(self):
        """
        Test that the office list view returns a status code of 200.
        """
        response = self.client.get(self.office_list_url)
        self.assertEqual(response.status_code, 200)

    def test_office_list_view_uses_correct_template(self):
        """
        Test that the office list view uses the correct template.
        """
        response = self.client.get(self.office_list_url)
        self.assertTemplateUsed(response, 'offices/office_list.html')

    def test_office_list_view_context(self):
        """
        Test that the office list view context contains the list of offices.
        """
        response = self.client.get(self.office_list_url)
        self.assertIn('object_list', response.context)
        offices = response.context['object_list']
        self.assertEqual(len(offices), 2)
        self.assertIn(self.office1, offices)
        self.assertIn(self.office2, offices)
