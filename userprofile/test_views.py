from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from datetime import date
from django.utils import timezone
from datetime import timedelta
from .models import UserProfile, Review, Booking
from .forms import UserProfileForm, ReviewForm
from cars.models import Car
from offices.models import Office


class MyProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username='testuser',
            password='testpassword',
            email="test@test.com"
        )
        self.client.login(username='testuser', password='testpassword')

    def test_view_creates_profile_and_displays_success_message(self):
        response = self.client.post(reverse('my_profile'), {
            'email': 'newemail@test.com',
            'first_name': 'Mike',
            'last_name': 'Buf',
            'date_of_birth': '2000-01-01',
            'phone': '+123456789'
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        messages_list = list(response.context['messages'])
        self.assertTrue(any(msg.message == 'Your profile has been updated successfully!' for msg in messages_list))

        expected_date_of_birth = date(2000, 1, 1)

        user_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(user_profile.email, 'newemail@test.com')
        self.assertEqual(user_profile.first_name, 'Mike')
        self.assertEqual(user_profile.last_name, 'Buf')
        self.assertEqual(user_profile.date_of_birth, expected_date_of_birth)
        self.assertEqual(user_profile.phone, '+123456789')

    def test_post_valid_form(self):
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
        """Проверяет обработку некорректных данных формы"""
        post_data = {
            'first_name': '',
            'last_name': '',
            'date_of_birth': '',
            'email': 'invalid-email',
            'phone': 'not-a-phone'
        }
        response = self.client.post(reverse('my_profile'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'email', 'Enter a valid email address.')


class LeaveReviewViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        self.car = Car.objects.create(
            make='Toyota',
            model='Corolla',
            type='Sedan',
            year=2020,
            seats=5,
            doors=4,
            fuel_type='Petrol',
            transmission='AT',
            air_conditioning=True,
            navigation=True,
            availability=True,
            price_per_day=50.00,
            image='path/to/car/image'
        )

        # Create office instances
        self.pickup_office = Office.objects.create(
            name='Downtown Office',
            phone_number='123-456-7890',
            latitude=40.712776,
            longitude=-74.005974,
            opening_time='08:00',
            closing_time='20:00'
        )

        self.booking = Booking.objects.create(
            user=self.user,
            pickup_office=self.pickup_office,
            return_office=self.pickup_office,
            start_date=timezone.now().date(),
            pick_up_time=timezone.now().time(),
            end_date=timezone.now().date() + timedelta(days=7),
            drop_off_time=timezone.now().time(),
            car=self.car,
            first_name='John',
            last_name='Doe',
            email='john.doe@example.com',
            phone_number='+1234567890',
            date_of_birth=timezone.now().date() - timedelta(days=365 * 30),  # Example value for 30 years ago
            child_seat=True,
            child_seat_option='Front',
            extra_insurance=True,
            rules_agreement=True,
            total_price=299.99,
            rental_days=7,
            status='completed'
        )

    def test_get_review_form(self):
        """Проверяет отображение формы для оставления отзыва"""
        self.assertTrue(self.client.login(username='testuser', password='testpassword'))

        response = self.client.get(reverse('leave_review', args=[self.booking.id]))

        # Check for successful response
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)
        self.assertIsInstance(response.context['form'], ReviewForm)

    # def test_post_valid_review(self):
    #     """Проверяет успешное создание отзыва"""
    #     post_data = {
    #         'rating': '5',
    #         'comment': 'Excellent service!',
    #         'is_anonymous': False
    #     }
    #     response = self.client.post(reverse('leave_review', args=[self.booking.id]), post_data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertTrue(Review.objects.filter(user=self.user).exists())

    # def test_post_invalid_review(self):
    #     """Проверяет обработку некорректных данных отзыва"""
    #     post_data = {
    #         'rating': '',
    #         'comment': '',
    #         'is_anonymous': False
    #     }
    #     response = self.client.post(reverse('leave_review', args=[self.booking.id]), post_data)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(response, 'form', 'rating', 'This field is required.')