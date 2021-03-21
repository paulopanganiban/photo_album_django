from .base import *
# development settings
# conda activate djphoto2.1
from .base import *
import os
# Override base.py settings here
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEBUG = True
ALLOWED_HOSTS = ['photo-album-project.eba-nqmsu5pk.us-west-2.elasticbeanstalk.com', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('RDS_DB_NAME'),
        'USER': os.environ.get('RDS_USERNAME'),
        'PASSWORD': os.environ.get('RDS_PASSWORD'),
        'HOST': os.environ.get('RDS_HOSTNAME'),
        'PORT': os.environ.get('RDS_PORT')
    }
}
# change directory of stored images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# media/profile_pics