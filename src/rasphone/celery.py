from __future__ import absolute_import

from celery import Celery
from conf import settings
from datetime import timedelta


app = Celery('rasphone',
             broker='amqp://',
             backend='amqp://',
             include=['rasphone.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=3600,
    CELERY_TIMEZONE='America/Lima',
    CELERYBEAT_SCHEDULE={
        'update-public-ip-every-hour': {
            'task': 'update-public-ip',
            'schedule': timedelta(minutes=settings.UPDATE_IP_TIME),
        },
    },
)

if __name__ == '__main__':
    app.start()
