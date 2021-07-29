from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, userUpdatefrom, profileUpateform
from django.contrib.auth.decorators import login_required


def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your account has been created! You are now able to log in.')
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form, 'pageTitle': 'Register'})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = userUpdatefrom(request.POST, instance=request.user)
        p_form = profileUpateform(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile info has been changed')
            return redirect('profile')
    else:
        u_form = userUpdatefrom(instance=request.user)
        p_form = profileUpateform(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'pageTitle': 'Profile'
    }

    return render(request, 'users/profile.html', context)
