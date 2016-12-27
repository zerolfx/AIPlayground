from django.contrib import admin
from .models import Problem
from .models import Sample

admin.site.register(Problem)
admin.site.register(Sample)