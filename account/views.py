from django.shortcuts import render, redirect
from .form import validator, ProfileForm
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect


@csrf_protect
def home(request):
    if request.method == 'POST':
        data = dict()
        validator_result = validator(request.POST)
        if validator_result['error']:
            data['error_message'] = validator_result['error']
        else:
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            data['message'] = validator_result['message']
            if request.GET.get('next'):
                return redirect(request.GET['next'])
        return render(request, 'index.html', data)
    else:
        return render(request, 'index.html')


# TODO add message
@login_required
def settings_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user_profile.email = form.cleaned_data.get('email')
            user_profile.save()
        return render(request, 'settings.html', {'form': form})
    else:
        form = ProfileForm(instance=user_profile, initial={
            'email': user_profile.email
        })
    return render(request, 'settings.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('/')
