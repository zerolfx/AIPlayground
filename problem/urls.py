from django.conf.urls import url
from .views import problem_feed, problem_view

urlpatterns = [
    url(r'^$', problem_feed, name='problem'),
    url(r'^(\d+)/', problem_view, name='problem_view'),
]