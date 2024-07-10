from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SearchForm
from offices.models import Office
from cars.models import Car
from django.http import JsonResponse
from django.urls import reverse


# Create your views here.
def booking_results(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            drop_off_time = form.cleaned_data['drop_off_time']
            pickup_office = form.cleaned_data['pickup_office']
            return_office = form.cleaned_data['return_office']

            # Here you can add filters based on the selected parameters
            cars = Car.objects.all()

            return render(request, 'bookings/booking.html', {
                'form': form,
                'cars': cars,
                'start_date': start_date,
                'end_date': end_date,
                'pick_up_time': pick_up_time,
                'drop_off_time': drop_off_time
            })
    else:
        initial_data = {
            'start_date': timezone.now().date(),
            'end_date': timezone.now().date() + timezone.timedelta(days=7),
        }
        form = SearchForm(initial=initial_data)
        dublin_airport = Office.objects.filter(name='Dublin Airport').first()
        if dublin_airport:
            form.update_pick_up_time_choices(dublin_airport.opening_time, dublin_airport.closing_time)
            form.update_drop_off_time_choices()

    return render(request, 'bookings/booking.html', {'form': form})

def update_pickup_time_choices(request):
    office_id = request.GET.get('office_id')
    office = Office.objects.get(id=office_id)
    form = SearchForm()
    choices = form.generate_pick_up_time_choices(office.opening_time, office.closing_time)
    return JsonResponse({'choices': list(choices)})


def home(request):
    return render(request, 'bookings/home.html')



