from django.db import models
from judge.models import Judge
from django.contrib.auth.models import User


class Sample(models.Model):

    input = models.FileField('Input')
    output = models.FileField('Output')


class Problem(models.Model):
    STATUS_CHOICES = (
        ('r', 'Removed'),
        ('a', 'Available'),
    )

    COMBAT_TYPE_CHOICES = (
        (1, 'Single'),
        (2, 'Combat'),
    )

    id = models.IntegerField('#', primary_key=True)
    title = models.CharField('Title', max_length=70)
    author = models.ForeignKey(User)
    submissions = models.IntegerField('Submissions', default=0)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
    likes = models.PositiveIntegerField('Likes', default=0)

    time_limit = models.IntegerField('Time Limit (ms)', default=1000)
    memory_limit = models.IntegerField('Memory Limit (MB)', default=512)
    program_limit = models.IntegerField('Program Limit (KB)', default=128)
    combat_type = models.IntegerField('Combat Type', choices=COMBAT_TYPE_CHOICES, default=1)
    description = models.TextField('Description')
    input = models.TextField('Input')
    output = models.TextField('Output')
    samples = models.ManyToManyField(Sample, blank=True)

    judge = models.ForeignKey(Judge, blank=True)

    def __str__(self):
        return str(self.id) + ' - ' + self.title

    class Meta:
        ordering = ['-id']

