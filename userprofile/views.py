from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import UserProfile, Review
from bookings.models import Booking
from .forms import UserProfileForm
from .forms import ReviewForm
from django.urls import reverse

# Create your views here.
@login_required
def my_profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(
            user=request.user,
            email=request.user.email,
            first_name='',
            last_name='',
            date_of_birth=None,
            phone=''
        )
    
    form = UserProfileForm(instance=user_profile)
    
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('my_profile')

        else:
            # If the form is invalid, collect form errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{form.fields[field].label}: {error}")
    
    context = {
        'form': form
    }
    return render(request, 'userprofile/my_profile.html', context)


def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    
    if booking.end_date == timezone.now().date() and booking.status == 'confirmed':
        booking.status = 'completed'
        booking.save()

    return redirect('my_bookings', booking_id=booking_id)

@login_required
def leave_review(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)

    if not booking.can_leave_review():
        # Redirect if review cannot be left
        return redirect(reverse('my_bookings'))

    
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
                    'Please rate, where one star is the lowest and 5 stars is the maximum score.'
                )
    else:
        form = ReviewForm()

    return render(request, 'userprofile/leave_review.html', {'form': form, 'booking': booking})


@login_required
def my_reviews(request):
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'userprofile/my_reviews.html', {'reviews': user_reviews})


def edit_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    booking = review.booking
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
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
                    'Please rate, where one star is the lowest and 5 stars is the maximum score.'
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
    review = get_object_or_404(Review, id=review_id)
    booking = review.booking
    if request.method == 'POST':
        booking.review_left = False
        booking.status = 'completed'
        booking.save()
        review.delete()
        messages.success(request, 'Review deleted successfully.')
        return redirect('my_reviews')

    return render(request, 'userprofile/confirm_delete_review.html', {'review': review, 'booking': booking})
