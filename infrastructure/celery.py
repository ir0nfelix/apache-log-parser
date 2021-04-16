import os
import django
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

app = Celery('apache-log-parser')
app.config_from_object('django.conf:settings', namespace='CELERY')
