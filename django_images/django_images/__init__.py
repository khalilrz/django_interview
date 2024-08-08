from __future__ import absolute_import, unicode_literals

# Import Celery module
from .celery_config import app as celery_app

__all__ = ('celery_app',)