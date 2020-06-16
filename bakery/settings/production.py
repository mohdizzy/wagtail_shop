from .dev import *
import os
AWS_SES_ACCESS_KEY_ID = os.environ.get('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = os.environ.get('AWS_SES_SECRET_ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

# AWS Postgres Aurora
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagshop',
        'USER': 'izzy',
        'PASSWORD': 'password123',
        'HOST': 'wagshop.cb1jr50xckkf.eu-west-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}

# Account verification flag
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

try:
    from .local import *
except ImportError:
    pass
