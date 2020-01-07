from .base import *
import environ

env = environ.Env(
    SECRET_KEY=str,
)

env_path = os.path.join(BASE_DIR, '.env')
environ.Env.read_env()


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY=env('SECRET_KEY')
ALLOWED_HOSTS = ['*']


#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


try:
    from .local import *
except ImportError:
    pass
