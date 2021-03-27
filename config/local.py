# # development settings
# # conda activate djphoto2.1
# from .base import *
# import os
# from decouple import config
# # Override base.py settings here
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEBUG = True
# ALLOWED_HOSTS = ['photo-album-project.eba-nqmsu5pk.us-west-2.elasticbeanstalk.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#     }
# }
# # change directory of stored images
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_URL = '/media/'
# # media/profile_pics