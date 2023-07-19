from .base import *

DEBUG = False
ALLOWED_HOSTS = ['54.225.71.199','doyeon0430.com','www.doyeon0430.com']

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '54.225.71.199:11211',  # Memcached 서버의 주소와 포트
    }
}