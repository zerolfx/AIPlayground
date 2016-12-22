from django.shortcuts import render

def status_view(request):
    return render(request, 'status.html')
