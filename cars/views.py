from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib import messages
from datetime import datetime
from bookings.forms import SearchForm
from offices.models import Office
from userprofile.models import UserProfile
from .models import Car


# Create your views here.
def car_search(request):
    """
    Handles the car search functionality.

    Renders the search form and displays available cars based on the search
    criteria.
    """
    car_types = Car.objects.values_list('type', flat=True).distinct()
    transmissions = Car.objects.values_list(
        'transmission', flat=True).distinct()

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            # Extract cleaned data from the form
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            drop_off_time = form.cleaned_data['drop_off_time']
            pickup_office = form.cleaned_data['pickup_office']
            return_office = form.cleaned_data['return_office']

            # Fetch and calculate car rental prices
            cars = Car.objects.filter(availability=True).order_by('make')
            cars = Car.calculate_car_rental_price(
                cars, start_date, end_date, pick_up_time, drop_off_time)

            # Render the booking results page
            return render(request, 'bookings/booking.html', {
                'form': form,
                'cars': cars,
                'car_types': car_types,
                'transmissions': transmissions,
                'start_date': start_date,
                'end_date': end_date,
                'pick_up_time': pick_up_time,
                'drop_off_time': drop_off_time,
                'pickup_office': pickup_office,
                'return_office': return_office,
            })
    else:
        initial_data = {
            'start_date': timezone.now().date() + timezone.timedelta(days=1),
            'end_date': timezone.now().date() + timezone.timedelta(days=8),
            'pick_up_time': '09:00',
            'drop_off_time': '09:00',
        }
        form = SearchForm(initial=initial_data)
        dublin_airport = Office.objects.filter(name='Dublin Airport').first()

    return render(request, 'bookings/booking.html', {
        'form': form
    })


def update_pickup_time_choices(request):
    """
    Updates the pick-up time choices based on the selected office's opening
    and closing times.

    Args:
        request (HttpRequest): The HTTP request object containing office ID.

    Returns:
        JsonResponse: JSON response with updated pick-up time choices.
    """
    office_id = request.GET.get('office_id')
    office = get_object_or_404(Office, id=office_id)
    form = SearchForm()
    choices = form.generate_pick_up_time_choices(
        office.opening_time, office.closing_time)
    return JsonResponse({'choices': list(choices)})


def update_car_list(request):
    """
    Updates the list of cars based on applied filters and sorting criteria.

    Args:
        request (HttpRequest): The HTTP request object containing filter and
        sort criteria.

    Returns:
        JsonResponse: JSON response with updated car list HTML.
    """
    car_type = request.GET.get('car_type')
    transmission = request.GET.get('transmission')
    sort_by = request.GET.get('sort_by', 'make')
    air_conditioning = request.GET.get('air_conditioning')
    navigation = request.GET.get('navigation')
    start_date = datetime.strptime(
        request.GET.get('start_date'), "%Y-%m-%d").date()
    end_date = datetime.strptime(
        request.GET.get('end_date'), "%Y-%m-%d").date()
    pick_up_time = request.GET.get('pick_up_time')
    drop_off_time = request.GET.get('drop_off_time')
    pickup_office = request.GET.get('pickup_office')
    return_office = request.GET.get('return_office')
    is_authenticated = request.user.is_authenticated

    # Filter cars by availability
    cars = Car.objects.filter(availability=True)

    # Apply filters if specified
    if car_type != 'all':
        cars = cars.filter(type=car_type)
    if transmission != 'all':
        cars = cars.filter(transmission=transmission)
    if air_conditioning == 'true':
        cars = cars.filter(air_conditioning=True)
    if navigation == 'true':
        cars = cars.filter(navigation=True)

    # Sort the cars
    if sort_by == 'price_asc':
        cars = cars.order_by('price_per_day')
    elif sort_by == 'price_desc':
        cars = cars.order_by('-price_per_day')
    else:
        cars = cars.order_by('make')

    cars = Car.calculate_car_rental_price(
        cars, start_date, end_date, pick_up_time, drop_off_time)

    context = {
        'cars': cars,
        'user': request.user,
        'start_date': start_date,
        'end_date': end_date,
        'pick_up_time': pick_up_time,
        'drop_off_time': drop_off_time,
        'pickup_office': pickup_office,
        'return_office': return_office,
    }

    html = render_to_string('bookings/car_list.html', context)

    return JsonResponse({
        'html': html,
        'is_authenticated': request.user.is_authenticated
    })
