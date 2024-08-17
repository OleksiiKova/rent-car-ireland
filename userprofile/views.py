from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from .models import UserProfile, Review
from bookings.models import Booking
from .forms import UserProfileForm, ReviewForm, ContactForm, SignUpForm


# Create your views here.
@login_required
def my_profile_view(request):
    """
    View for displaying and updating the current user's profile.

    Retrieves the UserProfile instance for the logged-in user, or creates
    one if it doesn't exist.
    Handles both GET (to display the form) and POST (to update the profile)
    requests. Displays
    success or error messages based on the form submission result.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with the user profile form.
    """
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        # If profile doesn't exist, create a new one with default values
        user_profile = UserProfile.objects.create(
            user=request.user,
            email=request.user.email,
            first_name='',
            last_name='',
            date_of_birth=None,
            phone=''
        )

    # Create a form instance with the user's profile
    form = UserProfileForm(instance=user_profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('my_profile')

        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(
                        request, f"{form.fields[field].label}: {error}")

    context = {
        'form': form
    }
    return render(request, 'userprofile/my_profile.html', context)


def update_booking_status(request, booking_id):
    """
    View for updating the status of a booking to 'completed' if the
    end date has passed and the booking status is 'confirmed'.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking to update.

    Returns:
        HttpResponse: Redirect to the 'my_bookings' view.
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if (booking.end_date == today and
            booking.status == 'confirmed'):
        booking.status = 'completed'
        booking.save()

    return redirect('my_bookings', booking_id=booking_id)


@login_required
def leave_review(request, booking_id):
    """
    View for submitting a review for a specific booking.

    Checks if the user is allowed to leave a review for the specified booking.
    Handles both GET (to display the review form) and POST (to submit the
    review) requests.
    Updates the booking status and sets review-related fields accordingly.
    Displays success or error messages based on the form submission result.

    Args:
        request (HttpRequest): The HTTP request object.
        booking_id (int): The ID of the booking for which to leave a review.

    Returns:
        HttpResponse: Rendered HTML page with the review form or redirect
        based on the result.
    """
    booking = get_object_or_404(Booking, pk=booking_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.booking = booking
            review.user = request.user
            review.save()
            booking.review_left = True
            booking.status = 'reviewed'
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has been sent successfully!'
            )
            return redirect(reverse('my_reviews'))
        else:
            if 'rating' in form.errors:
                messages.add_message(
                    request, messages.ERROR,
                    'Please rate, where one star is the lowest and 5 stars is '
                    'the maximum score.'
                )
    else:
        if booking.review_left:
            return redirect(reverse('my_reviews'))
        form = ReviewForm()
        return render(request, 'userprofile/leave_review.html', {
            'form': form, 'booking': booking})

    return render(request, 'userprofile/leave_review.html',
                  {'form': form, 'booking': booking})


@login_required
def my_reviews(request):
    """
    View for displaying the current user's reviews.

    Retrieves all reviews submitted by the logged-in user, ordered by
    creation date in descending order.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying the user's reviews.
    """
    user_reviews = (Review.objects
                    .filter(user=request.user)
                    .order_by('-created_at'))
    return render(request, 'userprofile/my_reviews.html',
                  {'reviews': user_reviews})


def edit_review(request, review_id):
    """
    View for editing a specific review.

    Retrieves the review to be edited and handles both GET (to display the
    form) and POST (to update the review) requests. Updates the review and
    its associated booking status if the form is valid. Displays success or
    error messages based on the form submission result.

    Args:
        request (HttpRequest): The HTTP request object.
        review_id (int): The ID of the review to edit.

    Returns:
        HttpResponse: Rendered HTML page with the review edit form or
        redirect based on the result.
    """
    review = get_object_or_404(Review, id=review_id)
    booking = review.booking

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            # Mark the review as not approved
            review.approved = False
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your review has been changed successfully!'
            )
            return redirect('my_reviews')
        else:
            if 'rating' in form.errors:
                messages.add_message(
                    request, messages.ERROR,
                    'Please rate, where one star is the lowest and 5 stars is '
                    'the maximum score.'
                )
    else:
        form = ReviewForm(instance=review)
    context = {
        'form': form,
        'booking': booking,
        'review': review
    }
    return render(request, 'userprofile/edit_review.html', context)


def delete_review(request, review_id):
    """
    View for deleting a specific review.

    Handles POST requests to delete the review and updates the associated
    booking's status.
    Displays a success message and redirects to the 'my_reviews' view.

    Args:
        request (HttpRequest): The HTTP request object.
        review_id (int): The ID of the review to delete.

    Returns:
        HttpResponse: Rendered HTML page with a confirmation message or
        redirect based on the result.
    """
    review = get_object_or_404(Review, id=review_id)
    booking = review.booking
    if request.method == 'POST':
        booking.review_left = False
        booking.status = 'completed'
        booking.save()
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('my_reviews')

    return render(request, 'userprofile/confirm_delete_review.html',
                  {'review': review, 'booking': booking})


def contact_us(request):
    """
    View for displaying and handling the contact form.

    Handles both GET (to display the form) and POST (to submit the message)
    requests.
    Displays success or error messages based on the form submission result.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page with the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We '
                             'endeavour to respond within 2 working days!')
            return redirect('home')
        else:
            messages.add_message(
                request, messages.ERROR,
                'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'userprofile/contact_us.html', {'form': form})


def home(request):
    """
    View for displaying the home page with approved reviews.

    Retrieves and displays all approved reviews, ordered by creation date
    in descending order.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying approved reviews.
    """
    reviews = Review.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'userprofile/home.html', {'reviews': reviews})


def all_reviews(request):
    """
    View for displaying all approved reviews with pagination.

    Retrieves all approved reviews, applies pagination, and renders the
    reviews list.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered HTML page displaying paginated reviews.
    """
    review_list = Review.objects.filter(approved=True).order_by('-created_at')
    paginator = Paginator(review_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'reviews': page_obj.object_list,
        'page_obj': page_obj,
        'is_paginated': page_obj.has_other_pages(),
    }
    return render(request, 'userprofile/all_reviews.html', context)
