from django.db import models
from problem.models import Problem
from django.contrib.auth.models import User


class Submission(models.Model):
    LANG_CHOICES = (
        ('c', 'C++'),
        ('j', 'Java'),
        ('p', 'Python')
    )

    VERDICT_STATUS = (
        (100, 'Waiting'),
        (101, 'Running'),
        (102, 'Pretest Passed (Past)'),
        (130, 'Compile Error'),

        # Status for AI Playground
        (200, 'Locked'),
        (201, 'Pretest Passed'),
        (202, 'Running on Contest'),
        (400, 'Rejected'),

        # Status for Online Judge
        (1000, 'Accepted'),
        (1001, 'Wrong Answer'),
        (1002, 'Time Limit Exceeded'),
        (1003, 'Memory Limit Exceeded'),
        (1004, 'Runtime Error'),

    )

    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(User)
    language = models.CharField('Language', max_length=1, choices=LANG_CHOICES)
    code = models.TextField('Code')
    submit_time = models.DateTimeField('Submit Time', auto_now=True)
    verdict = models.IntegerField('Verdict', choices=VERDICT_STATUS, null=True, blank=True)
    running_time = models.IntegerField('Running Time (ms)', null=True, blank=True)
    running_memory = models.IntegerField('Running Memory (KB)', null=True, blank=True)
    score = models.IntegerField('Score', default=0)
    rating = models.IntegerField('Rating', default=0)

    def __str__(self):
        return 'Submission #' + str(self.id)


class Run(models.Model):
    submission = models.ForeignKey(Submission)
    running_time = models.IntegerField('Running Time (ms)')
    running_memory = models.IntegerField('Running Memory (KB)')
    score = models.IntegerField('Gained Score')

