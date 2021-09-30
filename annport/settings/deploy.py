from .base import *

DEBUG = False

ALLOWED_HOSTS = ['3.38.69.237', 'annport.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Static, media
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/annport/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/annport/media'

DATA_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024
