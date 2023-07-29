import os
from celery import Celery
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')

app = Celery('config')

app.config_from_object('django.conf:settings', namespace='CELERY')

CELERY_BROKER_URL = 'redis://54.225.71.199:6379/0'
CELERY_RESULT_BACKEND = 'redis://54.225.71.199:6379/0'

# 스케줄 설정 추가
CELERY_BEAT_SCHEDULE = {
    'update_cache_task': {
        'task': 'myprofile.tasks.update_cache',
        'schedule': timedelta(minutes=1),  # 1분에 한 번씩 업데이트
    },
}

app.autodiscover_tasks()

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')