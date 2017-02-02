from django.conf.urls import url
from .views import problem_feed

urlpatterns = [
    url(r'^$', problem_feed, name='problem'),
]