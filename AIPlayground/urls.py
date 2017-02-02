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

from user.views import logout, sign_view, login_view, register_view, profile_view
from home.views import home_view
from problem.views import problist_view, problem_view
from submission.views import submission_view, submit
from status.views import status_view
from tests.views import vue_test

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home_view, name='home'),
    url(r'^login/', login_view, name='login'),
    url(r'^register/', register_view, name='register'),
    url(r'^logout/', logout, name='logout'),
    url(r'^problem/$', home_view, name='problem'),
    url(r'^competition/', home_view, name='competition'),
    url(r'^board/', home_view, name='board'),
    url(r'^sign/', sign_view, name='sign'),
    url(r'^user/$', home_view, name='user'),
    url(r'^search/$', home_view, name='search')
    # url(r'^problist/', problist_view, name='problist'),
    # url(r'^settings/', include('user.urls', namespace='settings', app_name='user')),
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
