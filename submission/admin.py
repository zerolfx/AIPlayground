from django.contrib import admin
from .models import Run
from .models import Round
from .models import Submission


admin.site.register(Run)
admin.site.register(Round)
admin.site.register(Submission)