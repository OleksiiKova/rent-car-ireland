from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib import messages
from urllib.parse import urlencode
from datetime import datetime
from .forms import SearchForm, BookingForm
from offices.models import Office
from userprofile.models import UserProfile
from .models import Booking
from cars.models import Car


# Create your views here.
def parse_date(date_str):
    """
    Parses a date string into a date object.

    Args:
        date_str (str): The date string to parse.

    Returns:
        datetime.date: The parsed date object.

    Raises:
        ValueError: If the date format is not supported.
    """
    try:
        return datetime.strptime(date_str, "%d %B %Y").date()
    except ValueError:
        raise ValueError(f"Date format for '{date_str}' is not supported.")


def get_office_by_id(office_id):
    """
    Retrieves an Office object by its ID.

    Args:
        office_id (int): The ID of the office.

    Returns:
        Office: The Office object if found, otherwise None.
    """
    try:
        return Office.objects.get(id=office_id)
    except Office.DoesNotExist:
        return None


def get_user_profile_data(user):
    """
    Retrieves the user profile data for the given user.

    Args:
        user (User): The user whose profile data is to be retrieved.

    Returns:
        dict: A dictionary containing the user profile data.
    """
    try:
        profile = user.userprofile
        return {
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'email': profile.email,
            'phone_number': profile.phone,
            'date_of_birth': profile.date_of_birth,
        }
    except UserProfile.DoesNotExist:
        return {}


def calc_rental_info(car, start_date, end_date, pick_up_time, drop_off_time):
    """
    Calculates the rental information for a given car and rental period.

    Args:
        car (Car): The car being rented.
        start_date (datetime.date): The start date of the rental period.
        end_date (datetime.date): The end date of the rental period.
        pick_up_time (str): The pickup time for the rental.
        drop_off_time (str): The drop-off time for the rental.

    Returns:
        tuple: A tuple containing the rental days and total cost, or
        (None, None) if no rental info is available.
    """
    rental_info = Car.calculate_final_price(
        [car], start_date, end_date, pick_up_time, drop_off_time
    )
    if rental_info:
        car_with_price = rental_info[0][0]
        rental_days = rental_info[0][1]
        total_cost = rental_info[0][2]
        return rental_days, total_cost
    return None, None


def handle_post_request(
    request,
    initial_data,
    car,
    car_id,
    rental_days,
    total_cost
):
    """
    Handles the POST request for the booking form.

    Args:
        request (HttpRequest): The HTTP request object.
        initial_data (dict): Initial data for the booking form.
        car (Car): The car being booked.
        rental_days (int): The number of rental days.
        total_cost (decimal.Decimal): The total cost of the rental.

    Returns:
        HttpResponse: The response to the POST request, either rendering the
        form again or redirecting to 'my_bookings'.
    """
    form = BookingForm(request.POST, initial=initial_data)
    if form.is_valid():
        booking = form.save(commit=False)
        booking.user = request.user
        if not booking.rules_agreement:
            messages.add_message(
                request, messages.ERROR,
                'You must agree to the rules before booking!'
            )
            return render(request, 'bookings/booking_form.html', {
                'form': form,
                'car': car,
                'rental_days': rental_days,
                'total_cost': total_cost,
            })

        # Check if the car is still available
        try:
            car = Car.objects.get(id=car_id, availability=True)
        except Car.DoesNotExist:
            messages.add_message(
                request, messages.ERROR,
                'Sorry, this car is no longer available. '
                'Please choose another car.'
            )
            return render(request, 'bookings/booking_form.html', {
                'form': form,
                'car': car,
                'rental_days': rental_days,
                'total_cost': total_cost,
            })
        booking.save()
        messages.add_message(
            request, messages.SUCCESS,
            'Your booking has been completed successfully!'
        )
        return redirect('my_bookings')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.add_message(
                    request, messages.ERROR,
                    f"{form.fields[field].label}: {error}"
                )
        return render(request, 'bookings/booking_form.html', {
            'form': form,
            'car': car,
            'rental_days': rental_days,
            'total_cost': total_cost,
        })


def booking_form(request, car_id):
    """
    Displays and processes the booking form for a specific car.

    Args:
        request (HttpRequest): The HTTP request object.
        car_id (int): The ID of the car being booked.

    Returns:
        HttpResponse: The rendered booking form or a redirect to 'my_bookings'
        after successful submission.

    **Context**

    ``car``
        The car being booked.
    ``rental_days``
        The number of rental days.
    ``total_cost``
        The total cost of the rental.
    ``form``
        The booking form.

    **Template:**

    :template:`bookings/booking_form.html`
    """
    car = get_object_or_404(Car, id=car_id)
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')
    pick_up_time = request.GET.get('pick_up_time')
    drop_off_time = request.GET.get('drop_off_time')
    pickup_office_id = request.GET.get('pickup_office')
    return_office_id = request.GET.get('return_office')

    try:
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)
    except ValueError as e:
        return HttpResponse(f"Error parsing date: {e}", status=400)

    pickup_office = get_office_by_id(pickup_office_id)
    return_office = get_office_by_id(return_office_id)

    rental_days, total_cost = calc_rental_info(
        car, start_date, end_date, pick_up_time, drop_off_time
    )

    initial_data = {
        'car': car,
        'start_date': start_date,
        'end_date': end_date,
        'pick_up_time': pick_up_time,
        'drop_off_time': drop_off_time,
        'pickup_office': pickup_office,
        'return_office': return_office,
    }

    if request.user.is_authenticated:
        initial_data.update(get_user_profile_data(request.user))

    car = Car.objects.get(id=car_id)
    if request.method == 'POST':
        return handle_post_request(
            request, initial_data, car, car_id, rental_days, total_cost
        )
    else:
        form = BookingForm(initial=initial_data)

    return render(request, 'bookings/booking_form.html', {
        'form': form,
        'car': car,
        'rental_days': rental_days,
        'total_cost': total_cost,
    })


@login_required
def my_bookings(request):
    """
    Displays the list of bookings for the logged-in user.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered template with user bookings.
    """
    user_bookings = (
        Booking.objects
        .filter(user=request.user)
        .order_by('-created_at')
    )
    return render(
        request, 'bookings/my_bookings.html', {'bookings': user_bookings}
    )


def edit_booking(request, booking_id):
    """
    Allows the user to edit an existing booking.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to edit.

    Returns:
        HttpResponse: The rendered template for editing the booking or redirect
        to 'my_bookings'.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    car = booking.car

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            if not booking.rules_agreement:
                messages.add_message(
                    request, messages.ERROR,
                    'You must agree to the rules before booking!'
                )
                return render(request, 'bookings/edit_booking.html', {
                    'form': form,
                    'car': car,
                })
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your booking has been changed successfully!'
            )
            return redirect('my_bookings')
    else:
        form = BookingForm(instance=booking)
        form.initial['rules_agreement'] = False

    return render(
        request, 'bookings/edit_booking.html', {'form': form, 'car': car}
    )


def delete_booking(request, booking_id):
    """
    Allows the user to delete an existing booking.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to delete.

    Returns:
        HttpResponse: The rendered template for confirming the deletion or
        redirect to 'my_bookings'.
    """
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking has been deleted successfully.')
        return redirect('my_bookings')

    return render(
        request, 'bookings/confirm_delete.html', {'booking': booking}
    )


def booking_details(request, booking_id):
    """
    Retrieves the details of a specific booking and returns them as JSON.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to retrieve details for.

    Returns:
        JsonResponse: The booking details as JSON.
    """
    try:
        booking = get_object_or_404(Booking, id=booking_id)
        car = booking.car

        data = {
            'car_model': car.model,
            'car_make': car.make,
            'car_year': car.year,
            'car_type': car.type,
            'car_fuel_type': car.fuel_type,
            'car_transmission': car.transmission,
            'car_seats': car.seats,
            'car_doors': car.doors,
            'car_air_conditioning': car.air_conditioning,
            'car_navigation': car.navigation,
            'car_price_per_day': car.price_per_day,
            'car_image': car.image.url,
            'booking_start_date': booking.start_date,
            'booking_end_date': booking.end_date,
            'booking_pick_up_time': booking.pick_up_time,
            'booking_drop_off_time': booking.drop_off_time,
            'booking_child_seat': booking.child_seat,
            'booking_child_seat_option': booking.child_seat_option,
            'booking_extra_insurance': booking.extra_insurance,
            'booking_rental_days': booking.rental_days,
            'booking_review_left': booking.review_left,
            'booking_status': booking.status,
            'customer_first_name': booking.first_name,
            'customer_last_name': booking.last_name,
            'customer_phone_number': booking.phone_number,
            'customer_email': booking.email,
            'customer_date_of_birth': booking.date_of_birth,
            'pickup_office': booking.pickup_office.name,
            'return_office': booking.return_office.name,
            'total_price': booking.total_price,
        }

        return JsonResponse(data)
    except Booking.DoesNotExist:
        return JsonResponse({'error': 'Booking not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


def get_car_details(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        data = {
            'car_model': car.model,
            'car_make': car.make,
            'car_year': car.year,
            'car_type': car.type,
            'car_fuel_type': car.fuel_type,
            'car_transmission': car.transmission,
            'car_seats': car.seats,
            'car_doors': car.doors,
            'car_air_conditioning': car.air_conditioning,
            'car_navigation': car.navigation,
            'car_price_per_day': car.price_per_day,
            'car_image': car.image.url,
        }
        return JsonResponse(data)
    except Car.DoesNotExist:
        return JsonResponse({'error': 'Car not found'}, status=404)
