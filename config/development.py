from .base import *
# development settings
# conda activate djphoto2.1
from .base import *
import os
# Override base.py settings here
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
DEBUG = True
ALLOWED_HOSTS = ['photo-album-project.eba-nqmsu5pk.us-west-2.elasticbeanstalk.com', '127.0.0.1']
SECRET_KEY = os.environ['SECRET_KEY']
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ['RDS_DB_NAME'],
            'USER': os.environ['RDS_USERNAME'],
            'PASSWORD': os.environ['RDS_PASSWORD'],
            'HOST': os.environ['RDS_HOSTNAME'],
            'PORT': os.environ['RDS_PORT'],
        }
    }
# change directory of stored images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
# media/profile_pics