from django_cron import CronJobBase, Schedule
from .models import Booking
from django.utils import timezone


class UpdateBookingStatusCronJob(CronJobBase):
    """
    Cron job to update the status of bookings that have ended.

    This job runs periodically and updates the status of bookings where
    the end date is earlier than the current date and the status is still
    'confirmed'. The status of such bookings is changed to 'completed'.

    Attributes:
        code (str): A unique identifier for this cron job.
    """
    code = 'bookings.update_booking_status'

    today = timezone.now().date()
    bookings = Booking.objects.filter(end_date__lt=today, status='confirmed')
    for booking in bookings:
        booking.status = 'completed'
        booking.save()
