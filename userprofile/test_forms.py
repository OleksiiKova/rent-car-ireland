from django.test import TestCase
from .forms import UserProfileForm, ReviewForm, ContactForm
from .models import UserProfile, Review, ContactMessage


class UserProfileFormTest(TestCase):
    """
    Tests for the UserProfileForm.
    """
    def test_valid_form(self):
        """
        Tests that the UserProfileForm accepts valid data.
        """
        form_data = {
            'first_name': 'Mike',
            'last_name': 'Buf',
            'date_of_birth': '2000-01-01',
            'email': 'test@test.com',
            'phone': '+1234567890'
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Valid form should be accepted')

    def test_invalid_phone_number(self):
        """
        Tests that the UserProfileForm rejects invalid phone numbers.
        """
        form_data = {
            'first_name': 'Mike',
            'last_name': 'Buf',
            'date_of_birth': '2000-01-01',
            'email': 'test@test.com',
            'phone': '1234567890'
        }
        form = UserProfileForm(data=form_data)
        self.assertFalse(
            form.is_valid(), msg='Invalid phone number should be rejected')

    def test_empty_some_fields(self):
        """
        Tests that the UserProfileForm accepts empty values for some fields.
        """
        form_data = {
            'first_name': 'Mike',
            'last_name': '',
            'date_of_birth': '',
            'email': 'test@test.com',
            'phone': ''
        }
        form = UserProfileForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Empty fields should be accepted')


class ReviewFormTest(TestCase):
    """
    Tests for the ReviewForm.
    """

    def test_valid_form(self):
        """
        Tests that the ReviewForm accepts valid data.
        """
        form_data = {
            'rating': '5',
            'comment': 'Excellent service!',
            'is_anonymous': False
        }
        form = ReviewForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Valid form should be accepted')

    def test_invalid_rating(self):
        """
        Tests that the ReviewForm rejects invalid ratings.
        """
        form_data = {
            'rating': '6',
            'comment': 'Excellent service!',
            'is_anonymous': False
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(
            form.is_valid(), msg='Invalid rating should be rejected')

    def test_empty_comment(self):
        """
        Tests that the ReviewForm rejects empty comments.
        """
        form_data = {
            'rating': '5',
            'comment': '',
            'is_anonymous': False
        }
        form = ReviewForm(data=form_data)
        self.assertFalse(
            form.is_valid(), msg='Empty comment should be rejected')


class ContactFormTest(TestCase):
    """
    Tests for the ContactForm.
    """

    def test_valid_form(self):
        """
        Tests that the ContactForm accepts valid data.
        """
        form_data = {
            'name': 'Mike Buf',
            'email': 'test@test.com',
            'message': 'I need help with my account.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid(), msg='Valid form should be accepted')

    def test_invalid_email(self):
        """
        Tests that the ContactForm rejects invalid email addresses.
        """
        form_data = {
            'name': 'Mike Buf',
            'email': 'invalid-email',
            'message': 'I need help with my account.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(), msg='Invalid email should be rejected')

    def test_empty_message(self):
        """
        Tests that the ContactForm rejects empty messages.
        """
        form_data = {
            'name': 'Mike Buf',
            'email': 'test@test.com',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(
            form.is_valid(), msg='Empty message should be rejected')
