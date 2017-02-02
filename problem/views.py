from django.shortcuts import render
from .models import Problem
import markdown2


def problem_feed(request):
    return render(request, 'feed_problem.html')


def problem_view(request, get_id):
    problem = Problem.objects.get(id=get_id)
    problem.description = markdown2.markdown(problem.description, )
    # problem.input = markdown2.markdown(problem.input)
    # problem.output = markdown2.markdown(problem.output)
    return render(request, 'problem.html', {'problem': problem, 'problist_active': 'active'})

