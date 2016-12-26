from django.shortcuts import render, redirect
from .form import validator, ProfileForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse
from django.contrib import messages


@csrf_protect
def account_submit(request, action_type):
    data = dict()
    validator_result = validator(request.GET, action_type)
    if validator_result['error']:
        data['error'] = 1
        data['message'] = validator_result['error']
    else:
        user = authenticate(username=request.GET['username'], password=request.GET['password'])
        login(request, user)
        data['error'] = 0
        data['message'] = validator_result['message']
    return JsonResponse(data)


@csrf_protect
def register_view(request):
    return account_submit(request, 'register')


@csrf_protect
def login_view(request):
    return account_submit(request, 'login')


@csrf_protect
def home(request):
    return render(request, 'index.html')


@login_required
def settings_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_profile.email = form.cleaned_data.get('email')
            user_profile.save()
            messages.add_message(request, messages.SUCCESS, 'Your profile was successfully edited.')
        return render(request, 'settings.html', {'form': form})
    else:
        form = ProfileForm(instance=user_profile, initial={
            'email': user_profile.email
        })
    return render(request, 'settings.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
