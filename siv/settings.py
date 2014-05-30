"""
Django settings for siv project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm+#ew*tbd6_5m%!-%bm@(7sb#=y!u^6=ygb=habg8w4plk#&jf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition
GRAPPELLI_ADMIN_TITLE = 'Sistema Virtual de Inscripciones'

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'careers',
    'home',
    'schedules',
    'semesters',
    'subjects',
    'teachers',
    'userstudents',
)
ACCOUNT_ACTIVATION_DAYS = 7

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'siv.urls'

WSGI_APPLICATION = 'siv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sistemasiv',#os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER':'root',
        'PASSWORD':'Marco.123',
        'HOST':'127.0.0.1',
        'PORT':'',
    }   

}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

import os
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = '/localhost/static'
STATIC_URL = 'http://localhost:8000/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'marco,itnl@gmail.com'
EMAIL_HOST_PASSWORD = '173283123'
EMAIL_PORT = 587

SITE_ID = 1