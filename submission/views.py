from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Submission
from .models import Run
from problem.models import Problem


def submission_view(request, get_id):
    submission = Submission.objects.get(id=get_id)
    problem = submission.problem
    return render(request, 'submission.html', {'problem': problem, 'submission': submission})


def submit(request):
    submission = Submission()
    submission.code = request.POST['code']
    submission.language = request.POST['languageSelect']
    submission.problem = Problem.objects.get(id=int(request.POST['problem_id']))
    submission.author = request.user
    submission.save()
    return HttpResponseRedirect(reverse('submission', args=(str(submission.id), )))

