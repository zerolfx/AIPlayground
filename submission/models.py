from django.db import models
from problem.models import Problem
from django.contrib.auth.models import User

VERDICT_STATUS = (
    (100, 'Waiting'),
    (101, 'Running'),
    (102, 'Pretest Passed (Past)'),
    (130, 'Compile Error'),
    (131, 'Waiting for Judge'),

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
    (1005, 'System Error'),

)


class Submission(models.Model):
    LANG_CHOICES = (
        ('c', 'C++'),
        ('j', 'Java'),
        ('p', 'Python')
    )

    problem = models.ForeignKey(Problem)
    author = models.ForeignKey(User)
    language = models.CharField('Language', max_length=1, choices=LANG_CHOICES)
    code = models.TextField('Code')
    submit_time = models.DateTimeField('Submit Time', auto_now_add=True)

    compile_error = models.TextField('Compile Error Message', null=True, blank=True)
    verdict = models.IntegerField('Verdict', choices=VERDICT_STATUS, null=True, blank=True)
    running_time = models.IntegerField('Running Time (ms)', null=True, blank=True)
    running_memory = models.IntegerField('Running Memory (KB)', null=True, blank=True)
    score = models.IntegerField('Score', default=0)
    rating = models.IntegerField('Rating', default=0)

    def __str__(self):
        return 'Submission #' + str(self.id)


class Round(models.Model):

    # There can be one or two or many (what?) submissions
    # Judge can be found in the related problem of the related submission...
    # A round can be played by one player (typically ACM Problems) or two players (AI Problems)
    submissions = models.ManyToManyField(Submission)

    # The corresponding runs are automatically attached to the round

    # All result can be found here
    # It will be formatted as: Player A scored xxx. Player B scored xxx.
    # The score will be stored temporarily in the submission field when running, and reset when rerunning.
    result = models.TextField('Judge Result', null=True, blank=True)


class Run(models.Model):
    round = models.ForeignKey(Round)
    running_time = models.IntegerField('Running Time (ms)', default=0)
    running_memory = models.IntegerField('Running Memory (KB)', default=0)
    input = models.FileField('Input', null=True, blank=True)
    output = models.FileField('Output', null=True, blank=True)
    message = models.TextField('Run Result Message', null=True, blank=True)
    result = models.IntegerField('Judge Result', choices=VERDICT_STATUS, default=100)

    def __str__(self):
        return 'Round ' + str(self.round.id) + ' #' + str(self.id)
