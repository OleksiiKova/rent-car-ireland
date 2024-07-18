from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib import messages

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