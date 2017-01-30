from django.shortcuts import render

def vue_test(request):
    return render(request, 'test.html')