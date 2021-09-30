from .base import *

DEBUG = False

ALLOWED_HOSTS = ['3.38.69.237', 'annport.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'annport',
        'USER': 'dbmasteruser',
        'PASSWORD': 'ajaF]dD^!cKwi,4HWn-!VK%>|Zm~dO7{',
        'HOST': 'ls-ad590dbf59aa2d32c41ac76e1c621a3dbd7da20c.czm6uidjjfmt.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Static, media
STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/annport/static'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static_files'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/ubuntu/annport/media'

DATA_UPLOAD_MAX_MEMORY_SIZE = 100*1024*1024
