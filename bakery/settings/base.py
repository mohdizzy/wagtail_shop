
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import environ


PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
env_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env()
env=environ.Env


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.settings',
    'wagtail.api.v2',


    'modelcluster',
    'taggit',
    'rest_framework',

    'longclaw.core',
    'longclaw.configuration',
    'longclaw.shipping',
    'longclaw.products',
    'longclaw.orders',
    'longclaw.checkout',
    'longclaw.basket',
    'longclaw.stats',

    'debug_toolbar',

    'home',
    'search',
    'catalog',
    'bakery',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'crispy_forms',
    'django_ses',
    'mathfilters',
    'responsive',
    'storages',
    'zappa_django_utils',

]

MIDDLEWARE = [

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'responsive.middleware.ResponsiveMiddleware',
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

ROOT_URLCONF = 'bakery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(PROJECT_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'longclaw.configuration.context_processors.currency',
                'wagtail.contrib.settings.context_processors.settings',
                'responsive.context_processors.device',
            ],
        },
    },
]

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379/1",
#         'TIMEOUT': '86400',
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

WSGI_APPLICATION = 'bakery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, 'static'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
#
# # S3 settings
# AWS_STORAGE_BUCKET_NAME = 'wagshop'
# AWS_S3_REGION_NAME = 'eu-west-1'  # e.g. us-east-2
#
#
#
# # Tell django-storages the domain to use to refer to static files.
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#
# # Tell the staticfiles app to use S3Boto3 storage when writing the collected static files (when
# # you run `collectstatic`).
# STATICFILES_LOCATION = 'static'
# STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#
#
# MEDIAFILES_LOCATION = 'media'
# DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'



# Wagtail settings

WAGTAIL_SITE_NAME = "bakery"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://miztique.io'

# Longclaw settings

# The payment gateway to use. `BasePayment` is a dummy payment gateway for testing.
# Longclaw also offers 'BraintreePayment', 'PaypalVZeroPayment' and 'StripePayment'
PAYMENT_GATEWAY = 'longclaw.checkout.gateways.BasePayment'

PRODUCT_VARIANT_MODEL = 'catalog.ProductVariant'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"
INTERNAL_IPS = ['127.0.0.1']

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

env = environ.Env(
    AWS_SES_ACCESS_KEY_ID=str,
    AWS_SES_SECRET_ACCESS_KEY=str,
)


EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_SES_ACCESS_KEY_ID = env('AWS_SES_ACCESS_KEY_ID')
AWS_SES_SECRET_ACCESS_KEY = env('AWS_SES_SECRET_ACCESS_KEY')
DEFAULT_FROM_EMAIL = 'contact@mohdizzy.com'
AWS_SES_REGION_NAME='eu-west-1'
AWS_SES_REGION_ENDPOINT='email.eu-west-1.amazonaws.com'

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_PRESERVE_USERNAME_CASING = False
ACCOUNT_FORMS = {'signup': 'bakery.forms.CustomSignupForm'}
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'mizqtique.io - '


CRISPY_TEMPLATE_PACK = 'bootstrap4'

