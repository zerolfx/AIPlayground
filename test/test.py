import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.extend([BASE_DIR])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIPlayground.settings")
django.setup()
# import django_manage_shell; django_manage_shell.run("/home/zerol/PycharmProjects/AIPlayground")

from submission.models import *
from core.runner import controller
import shutil


rd = Round.objects.all().first()
path = os.path.join(BASE_DIR, 'workspace', 'run', str(rd.id))
print(path)
if os.path.exists(path):
    shutil.rmtree(path)

controller(rd.id)
