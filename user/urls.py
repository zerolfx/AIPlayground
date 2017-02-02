from django.conf.urls import url
from .views import settings_profile, settings_security

urlpatterns = [
    url(r'^profile/', settings_profile, name='profile'),
    url(r'^security/', settings_security, name='security'),
    # url(r'^notification/', settings_notification, name='notification')
]