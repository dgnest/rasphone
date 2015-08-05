from __future__ import absolute_import

from datetime import timedelta

from celery import Celery
from celery.schedules import crontab


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
            'schedule': crontab(
                hour=0,
                minute=15,
            ),
        },
    },
    # CELERYBEAT_SCHEDULE={
    #     'update-public-ip-every-hour': {
    #         'task': 'update-public-ip',
    #         'schedule': timedelta(seconds=5),
    #     },
    # },
)

if __name__ == '__main__':
    app.start()
