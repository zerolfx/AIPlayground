from django.shortcuts import render, redirect
from .form import validator
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect
from core.views import home_view


@csrf_protect
def login_register(request):
    if request.method == 'POST':
        data = dict()
        validator_result = validator(request.POST)
        if validator_result['error']:
            data['error_message'] = validator_result['error']
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            data['message'] = validator_result['message']
        return home_view(request, data)


def logout(request):
    auth_logout(request)
    redirect('/')
