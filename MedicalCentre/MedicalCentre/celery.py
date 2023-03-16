import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MedicalCentre.settings")
app = Celery("MedicalCentre")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
