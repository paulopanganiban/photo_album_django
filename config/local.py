# development settings
# conda activate djphoto2.1
from .base import *
# Override base.py settings here
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'