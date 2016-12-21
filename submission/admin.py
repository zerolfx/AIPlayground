from django.contrib import admin
from .models import Run
from .models import Submission


admin.site.register(Run)
admin.site.register(Submission)