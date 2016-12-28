import sys; print('Python %s on %s' % (sys.version, sys.platform))
import django; print('Django %s' % django.get_version())
import os
sys.path.extend(['/home/zerol/PycharmProjects/AIPlayground', '/home/zerol/Software/pycharm/helpers/pycharm', '/home/zerol/Software/pycharm/helpers/pydev'])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "AIPlayground.settings")
django.setup()
# import django_manage_shell; django_manage_shell.run("/home/zerol/PycharmProjects/AIPlayground")

from submission.models import *
from core.runner import controller
import shutil
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = Round.objects.all().first()
path = os.path.join(BASE_DIR, 'workspace', 'run', str(rd.id))
print(path)
if os.path.exists(path):
    shutil.rmtree(path)

controller(rd.id)
