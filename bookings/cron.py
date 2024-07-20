from django_cron import CronJobBase, Schedule
from .models import Booking
from django.utils import timezone

class UpdateBookingStatusCronJob(CronJobBase):
    RUN_AT_TIMES = ['00:00']

    schedule = Schedule(run_at_times=RUN_AT_TIMES)
    code = 'bookings.update_booking_status'

    def do(self):
        today = timezone.now().date()
        bookings = Booking.objects.filter(end_date__lt=today, status='confirmed')
        for booking in bookings:
            booking.status = 'completed'
            booking.save()