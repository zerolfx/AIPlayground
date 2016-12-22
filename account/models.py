from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField('email', max_length=30, blank=True, unique=True)
    rating = models.IntegerField('rating', default=0)

    def __str__(self):
        return self.user.username + '-Profile'
