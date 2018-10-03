from tickets.settings.base import *


import environ
env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ksfjk23fj09sjf93j09sjf09j2039'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

ALLOWED_HOSTS = [
    "0.0.0.0",
    "django-task-example.cfapps.io",
    "tasks.cf.chkr.at",
]



DATABASES = {
    'default': env.db(),
}

