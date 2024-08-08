from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the environment for Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_images.settings')
# Initialize Celery
app = Celery('django_images')
# Load Celery configurations from the Django settings file
app.config_from_object('django.conf:settings', namespace='CELERY')
# Discovering tasks in Django applications
app.autodiscover_tasks()
