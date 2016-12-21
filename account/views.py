from django.shortcuts import render, redirect
from .form import validator
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def login_register(request):
    if request.method == 'POST':
        result = validator(request.POST)
        if result['error']:
            return render(request, 'index.html', {'error_message': result['error']})
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return render(request, 'index.html', {'message': result['message']})
    return redirect('/')


def logout(request):
    auth_logout(request)
    redirect('/')
