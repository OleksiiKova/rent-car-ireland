from django.utils import timezone
from django.contrib.auth.models import User
from datetime import timedelta
from .models import UserProfile, Review, Booking
from .forms import UserProfileForm, ReviewForm
from cars.models import Car
from offices.models import Office


def create_test_data():
    user = User.objects.create_user(
        username='testuser', password='testpassword')

    car = Car.objects.create(
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

    office = Office.objects.create(
        name='Main Office',
        phone_number='+123456789',
        latitude=40.712776,
        longitude=-74.005974,
        opening_time='08:00',
        closing_time='20:00'
    )

    booking = Booking.objects.create(
        user=user,
        pickup_office=office,
        return_office=office,
        start_date=timezone.now().date(),
        pick_up_time=timezone.now().time(),
        end_date=timezone.now().date() + timedelta(days=7),
        drop_off_time=timezone.now().time(),
        car=car,
        first_name='Mike',
        last_name='Buf',
        email='test@example.com',
        phone_number='+1234567890',
        date_of_birth=timezone.now().date() - timedelta(days=365 * 30),
        child_seat=True,
        child_seat_option='Front',
        extra_insurance=True,
        rules_agreement=True,
        total_price=299.99,
        rental_days=7,
        status='completed'
    )

    review = Review.objects.create(
        user=user,
        booking=booking,
        rating=5,
        comment='Excellent service!',
        created_at=timezone.now().date(),
        approved=True
        )

    return user, car, office, booking, review
