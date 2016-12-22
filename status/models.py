from django.db import models
from problem.models import Problem
from django.contrib.auth.models import User


class News(models.Model):
    STATUS_OPTION = (
        ('n', 'News'),
        ('c', 'Comment')
    )
    author = models.ForeignKey(User)
    content = models.TextField('Content')
    problem = models.ForeignKey(Problem)
    status = models.CharField('Status', max_length=1, choices=STATUS_OPTION)
