from django.shortcuts import render
from .models import Submission
from .models import Run
from problem.models import Problem


def submission_view(request, get_id):
    submission = Submission.objects.get(id=get_id)
    problem = Problem.objects.get(id=submission.problem_id)
    return render(request, 'submission.html', {'problem': problem, 'submission': submission})
