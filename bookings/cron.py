from django_cron import CronJobBase, Schedule
from .models import Booking
from django.utils import timezone


class UpdateBookingStatusCronJob(CronJobBase):
    code = 'bookings.update_booking_status'

    today = timezone.now().date()
    bookings = Booking.objects.filter(end_date__lt=today, status='confirmed')
    for booking in bookings:
        booking.status = 'completed'
        booking.save()