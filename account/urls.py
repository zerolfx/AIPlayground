from django.conf.urls import url
from .views import settings_profile

urlpatterns = [
    url(r'^profile/', settings_profile, name='profile')
]