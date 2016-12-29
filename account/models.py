from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField('Email', max_length=80, blank=True)
    first_name = models.CharField('First Name', max_length=30, blank=True)
    last_name = models.CharField('Last Name', max_length=30, blank=True)
    birth_date = models.DateField('Birth Date', blank=True)
    country = models.CharField('Country', max_length=30, blank=True)
    city = models.CharField('City', max_length=30, blank=True)
    organization = models.CharField('Organization', max_length=80, blank=True)

    rating = models.IntegerField('rating', default=0)

    def __str__(self):
        return self.user.username + '-Profile'
