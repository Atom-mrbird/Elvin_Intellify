from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

# set the default django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Usertest.settings')

app = Celery('Usertest', broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')

# load task modules from all registered django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))