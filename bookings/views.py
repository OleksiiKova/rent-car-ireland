from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import SearchForm
from offices.models import Office
from cars.models import Car
from django.http import JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string


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

            car_types = Car.objects.values_list('type', flat=True).distinct()
            transmissions = Car.objects.values_list('transmission', flat=True).distinct()

            return render(request, 'bookings/booking.html', {
                'form': form,
                'cars': cars,
                'car_types': car_types,
                'transmissions': transmissions,
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

        car_types = Car.objects.values_list('type', flat=True).distinct()
        transmissions = Car.objects.values_list('transmission', flat=True).distinct()

    return render(request, 'bookings/booking.html', {
        'form': form, 
        'car_types': car_types,
        'transmissions': transmissions,
        })

def update_pickup_time_choices(request):
    office_id = request.GET.get('office_id')
    office = Office.objects.get(id=office_id)
    form = SearchForm()
    choices = form.generate_pick_up_time_choices(office.opening_time, office.closing_time)
    return JsonResponse({'choices': list(choices)})


def home(request):
    return render(request, 'bookings/home.html')

# Update a list of car after applying filters
def update_car_list(request):
    car_type = request.GET.get('car_type')
    transmission = request.GET.get('transmission')
    sort_by = request.GET.get('sort_by')
    air_conditioning = request.GET.get('air_conditioning')
    navigation = request.GET.get('navigation')

    # Get all the cars
    cars = Car.objects.all()

    # Apply filters if specified
    if car_type != 'all':
        cars = cars.filter(type=car_type)
    if transmission != 'all':
        cars = cars.filter(transmission=transmission)
    if air_conditioning == 'true':
        cars = cars.filter(air_conditioning=True)
    if navigation == 'true':
        cars = cars.filter(navigation=True)
    if sort_by == 'price':
        cars = cars.order_by('price_per_day')
    
    cars = cars.order_by('make')

    if sort_by == 'price_asc':
        cars = cars.order_by('price_per_day')
    elif sort_by == 'price_desc':
        cars = cars.order_by('-price_per_day')
    
    context = {
        'cars': cars,
    }

    # Genere HTML for a list of cars
    html = render_to_string('bookings/car_list.html', {'cars': cars})

    # Return a JSON response with generated HTML
    return JsonResponse({'html': html})

