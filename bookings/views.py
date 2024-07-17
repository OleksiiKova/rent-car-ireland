from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages
from .forms import SearchForm, BookingForm
from offices.models import Office
from .models import Booking
from cars.models import Car
from django.http import JsonResponse
from django.urls import reverse
from django.template.loader import render_to_string
from urllib.parse import urlencode


# Create your views here.
def booking_search(request):
    car_types = Car.objects.values_list('type', flat=True).distinct()
    transmissions = Car.objects.values_list('transmission', flat=True).distinct()
    
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            pick_up_time = form.cleaned_data['pick_up_time']
            drop_off_time = form.cleaned_data['drop_off_time']
            pickup_office = form.cleaned_data['pickup_office']
            return_office = form.cleaned_data['return_office']

            cars = Car.objects.filter(availability=True).order_by('make')
            cars = Car.calculate_car_rental_price(cars, start_date, end_date, pick_up_time, drop_off_time)


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
    sort_by = request.GET.get('sort_by', 'make')
    air_conditioning = request.GET.get('air_conditioning')
    navigation = request.GET.get('navigation')
    start_date = datetime.strptime(request.GET.get('start_date'), "%Y-%m-%d").date()
    end_date = datetime.strptime(request.GET.get('end_date'), "%Y-%m-%d").date()
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

    cars = Car.calculate_car_rental_price(cars, start_date, end_date, pick_up_time, drop_off_time)

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

    # Generate HTML for a list of cars
    html = render_to_string('bookings/car_list.html', context)

    # Return a JSON response with generated HTML
    return JsonResponse({
        'html': html,
        'is_authenticated': request.user.is_authenticated
    })


def parse_date(date_str):
    for date_format in ("%B %d, %Y", "%b. %d, %Y"):
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue
    raise ValueError(f"Date format for '{date_str}' is not supported.")


def booking_form(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    # start_date = datetime.strptime(request.GET.get('start_date'), '%b. %d, %Y').date()
    # end_date = datetime.strptime(request.GET.get('end_date'), '%b. %d, %Y').date()
    pick_up_time = request.GET.get('pick_up_time')
    drop_off_time = request.GET.get('drop_off_time')
    pickup_office_id = request.GET.get('pickup_office')
    return_office_id = request.GET.get('return_office')
    
    try:
        # Use the helper function to parse the dates
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
    except ValueError as e:
        # Handle the error appropriately, e.g., return an error response
        return HttpResponse(f"Error parsing date: {e}", status=400)

    # Retrieving office objects by id
    try:
        pickup_office = Office.objects.get(id=pickup_office_id)
    except Office.DoesNotExist:
        pickup_office = None
    try:
        return_office = Office.objects.get(id=return_office_id)
    except Office.DoesNotExist:
        return_office = None

    # Calculate the rental price for the selected car
    rental_info = Car.calculate_final_price([car], start_date, end_date, pick_up_time, drop_off_time)

    # Unpack rental_info if it is not empty
    if rental_info:
        car_with_price = rental_info[0][0]
        rental_days = rental_info[0][1]
        total_cost = rental_info[0][2]
    else:
        rental_days = total_cost = None

    initial_data = {
        'car': car,
        'start_date': start_date,
        'end_date': end_date,
        'pick_up_time': pick_up_time,
        'drop_off_time': drop_off_time,
        'pickup_office': pickup_office,
        'return_office': return_office,
    }

    if request.method == 'POST':
        form = BookingForm(request.POST, initial=initial_data)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            if not booking.rules_agreement:
                messages.add_message(request, messages.ERROR,
                                 'You must agree to the rules before booking!')
                return render(request, 'bookings/booking_form.html', {
                    'form': form,
                    'car': car,
                    'rental_days': rental_days,
                    'total_cost': total_cost,
                    # 'start_date': start_date,
                    # 'end_date': end_date,
                    # 'pick_up_time': pick_up_time,
                    # 'drop_off_time': drop_off_time,
                    # 'pickup_office': pickup_office,
                    # 'return_office': return_office,
                })
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been completed successfully!'
            )
            return redirect('my_bookings')
        

    else:
        form = BookingForm(initial=initial_data)

    return render(request, 'bookings/booking_form.html', {
        'form': form, 
        'car': car,
        'rental_days': rental_days,
        'total_cost': total_cost,        
        # 'start_date': start_date,
        # 'end_date': end_date,
        # 'pick_up_time': pick_up_time,
        # 'drop_off_time': drop_off_time,
        # 'pickup_office': pickup_office,
        # 'return_office': return_office,
        })


@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': user_bookings})

