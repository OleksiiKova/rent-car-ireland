from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date, timedelta
from django.utils import timezone
from .models import UserProfile, Review, Booking
from .forms import UserProfileForm, ReviewForm
from cars.models import Car
from offices.models import Office
from .test_data import create_test_data


class MyProfileViewTest(TestCase):
    """
    Tests for the profile view which allows users to view and update their
    profile information.
    """
    def setUp(self):
        """
        Create a superuser and log in for the test cases.
        """
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email="test@test.com"
        )
        self.client.login(username='testuser', password='testpassword')

    def test_view_creates_profile_and_displays_success_message(self):
        """
        Test that the profile view updates user profile information and
        displays a success message.
        """
        response = self.client.post(reverse('my_profile'), {
            'email': 'newemail@test.com',
            'first_name': 'Mike',
            'last_name': 'Buf',
            'date_of_birth': '2000-01-01',
            'phone': '+123456789'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        messages_list = list(response.context['messages'])
        self.assertTrue(
            any(
                msg.message == 'Your profile has been updated successfully!'
                for msg in messages_list
            )
        )

        expected_date_of_birth = date(2000, 1, 1)

        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.email, 'newemail@test.com')
        self.assertEqual(user_profile.first_name, 'Mike')
        self.assertEqual(user_profile.last_name, 'Buf')
        self.assertEqual(user_profile.date_of_birth, expected_date_of_birth)
        self.assertEqual(user_profile.phone, '+123456789')

    def test_post_valid_form(self):
        """
        Test that a valid form submission updates the user profile.
        """
        post_data = {
            'first_name': 'Updated',
            'last_name': 'Name',
            'date_of_birth': '1990-01-01',
            'email': 'updated@example.com',
            'phone': '+0987654321'
        }
        response = self.client.post(reverse('my_profile'), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(UserProfile.objects.filter(user=self.user).exists())

    def test_post_invalid_form(self):
        """
        Test that an invalid form submission returns form errors.
        """
        post_data = {
            'first_name': '',
            'last_name': '',
            'date_of_birth': '',
            'email': 'invalid-email',
            'phone': 'not-a-phone'
        }
        response = self.client.post(reverse('my_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'email', 'Enter a valid email address.')


class LeaveReviewViewTest(TestCase):
    """
    Tests for the view that allows users to leave reviews for their bookings.
    """
    def setUp(self):
        """
        Create necessary test data and log in for the test cases.
        """
        self.user, self.car, self.pickup_office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

    def test_get_review_form(self):
        """
        Test that the review form is rendered correctly.
        """
        self.assertTrue(
            self.client.login(username='testuser', password='testpassword'))

        response = self.client.get(
            reverse('leave_review', args=[self.booking.id]))

        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_post_valid_review(self):
        """
        Test that a valid review is successfully submitted and saved.
        """
        Review.objects.filter(booking=self.booking).delete()

        post_data = {
            'rating': '5',
            'comment': 'Excellent service!',
            'is_anonymous': False
        }
        response = self.client.post(
            reverse('leave_review', args=[self.booking.id]), post_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Review.objects.filter(booking=self.booking).exists())

    def test_post_invalid_review(self):
        """
        Test that an invalid review submission returns form errors.
        """
        post_data = {
            'rating': '',
            'comment': '',
            'is_anonymous': False
        }
        response = self.client.post(reverse(
            'leave_review', args=[self.booking.id]), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'rating', 'This field is required.')


class MyReviewsViewTest(TestCase):
    """
    Tests for the view that displays the user's reviews.
    """

    def setUp(self):
        """
        Create necessary test data and log in for the test cases.
        """
        self.user, self.car, self.pickup_office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

    def test_view_my_reviews(self):
        """
        Test that the view correctly displays the user's reviews.
        """
        response = self.client.get(reverse('my_reviews'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Excellent service!')


class EditReviewViewTest(TestCase):
    """
    Tests for the view that allows users to edit their reviews.
    """

    def setUp(self):
        """
        Create necessary test data and log in for the test cases.
        """
        self.user, self.car, self.pickup_office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

    def test_get_edit_review_form(self):
        """
        Test that the review edit form is rendered correctly.
        """
        response = self.client.get(
            reverse('edit_review', args=[self.review.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], ReviewForm)

    def test_post_valid_edit_review(self):
        """
        Test that a valid edit to a review is successfully submitted and saved.
        """
        post_data = {
            'rating': '4',
            'comment': 'Very good service',
            'is_anonymous': False
        }
        response = self.client.post(reverse(
            'edit_review', args=[self.review.id]), post_data)
        self.review.refresh_from_db()
        self.assertEqual(self.review.rating, 4)
        self.assertEqual(self.review.comment, 'Very good service')
        self.assertEqual(response.status_code, 302)

    def test_post_invalid_edit_review(self):
        """
        Test that an invalid review edit submission returns form errors.
        """
        post_data = {
            'rating': '',
            'comment': '',
            'is_anonymous': False
        }
        response = self.client.post(reverse(
            'edit_review', args=[self.review.id]), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response, 'form', 'rating', 'This field is required.')


class DeleteReviewViewTest(TestCase):
    """
    Tests for the view that allows users to delete their reviews.
    """

    def setUp(self):
        """
        Create necessary test data and log in for the test cases.
        """
        self.user, self.car, self.pickup_office, self.booking, self.review = (
            create_test_data()
        )
        self.client.login(username='testuser', password='testpassword')

    def test_delete_review(self):
        """
        Test that a review is successfully deleted.
        """
        response = self.client.post(
            reverse('delete_review', args=[self.review.id]))
        self.assertEqual(response.status_code, 302)
