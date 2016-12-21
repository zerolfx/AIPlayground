from django.shortcuts import render
from .models import Problem

def problist_view(request):
    ProblemList = Problem.objects.filter(status='a')
    return render(request, 'problist.html', {'problem_list': ProblemList})

def problem_view(request, get_id):
    problem = Problem.objects.get(id=get_id)
    return render(request, 'problem.html', {'problem': problem})
