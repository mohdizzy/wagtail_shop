from .dev import *

DEBUG = False

# AWS Postgres Aurora
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wagshop',
        'USER': 'izzy',
        'PASSWORD': 'password123',
        'HOST': '',
        'PORT': '5432',
    }
}

try:
    from .local import *
except ImportError:
    pass
