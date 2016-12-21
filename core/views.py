from django.shortcuts import render
# Create your views here.


def home_view(request, data=None):
    if not data:
        data = dict()
    return render(request, 'index.html', data)
