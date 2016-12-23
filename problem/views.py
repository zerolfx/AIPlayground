from django.shortcuts import render
from .models import Problem
import markdown2


def problist_view(request):
    ProblemList = Problem.objects.filter(status='a')
    return render(request, 'problist.html', {'problem_list': ProblemList, 'problist_active': 'active'})


def problem_view(request, get_id):
    problem = Problem.objects.get(id=get_id)
    problem.description = markdown2.markdown(problem.description, )
    problem.input = markdown2.markdown(problem.input)
    problem.output = markdown2.markdown(problem.output)
    return render(request, 'problem.html', {'problem': problem, 'problist_active': 'active'})

