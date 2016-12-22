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
from django.conf.urls import url, include
from django.contrib import admin

from account.views import home, logout
from problem.views import problist_view, problem_view
from submission.views import submission_view
from status.views import status_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^logout/', logout, name='logout'),
    url(r'^problist/', problist_view, name='problist'),
    url(r'^settings/', include('account.urls', namespace='settings', app_name='account')),
    url(r'^problem/(\d+)/', problem_view, name='problem'),
    url(r'^submission/(\d+)', submission_view, name='submission'),
    url(r'^status/', status_view, name='status')
]
