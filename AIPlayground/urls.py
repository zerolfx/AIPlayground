"""AIPlayground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin

from account.views import home, logout, login_view, register_view, profile_view
from problem.views import problist_view, problem_view
from submission.views import submission_view, submit
from status.views import status_view
from tests.views import vue_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout, name='logout'),
    url(r'^problem/$', home, name='problem'),
    url(r'^competition/', home, name='competition'),
    url(r'^board/', home, name='board'),
    url(r'^sign/', home, name='sign')
    # url(r'^problist/', problist_view, name='problist'),
    # url(r'^settings/', include('account.urls', namespace='settings', app_name='account')),
    # url(r'^problem/(\d+)/', problem_view, name='problem'),
    # url(r'^submission/(\d+)', submission_view, name='submission'),
    # url(r'^submit/', submit, name='submit'),
    # url(r'^status/', status_view, name='status'),
    # url(r'^profile/(.+)/', profile_view, name='profile'),
    # url(r'^test/', vue_test)
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
