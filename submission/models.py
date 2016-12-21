from django.db import models


class Run(models.Model):
    running_time = models.IntegerField('Running Time (ms)')
    running_memory = models.IntegerField('Running Memory (KB)')
    score = models.IntegerField('Gained Score')


class Submission(models.Model):
    LANG_CHOICES = (
        ('c', 'C++'),
        ('j', 'Java'),
        ('p', 'Python')
    )

    VERDICT_STATUS = (
        # Status for AI Playground
        (100, 'Waiting'),
        (101, 'Running on Pretest'),
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

    language = models.CharField('Language', max_length=1, choices=LANG_CHOICES)
    code = models.TextField('Code')
    code_length = models.IntegerField('Code Length')
    submit_time = models.DateTimeField('Submit Time', auto_now=True)
    verdict = models.IntegerField('Verdict', choices=VERDICT_STATUS)
    score = models.IntegerField('Score', default=0)
    rating = models.IntegerField('Rating', default=0)

    running_data = models.ManyToManyField(Run, 'Running')

