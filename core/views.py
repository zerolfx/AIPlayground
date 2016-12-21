from django.shortcuts import render
# Create your views here.


def home_view(request):
    data = dict()
    if request.user:
        data['title'] = request.user.username
    return render(request, 'index.html', data)
