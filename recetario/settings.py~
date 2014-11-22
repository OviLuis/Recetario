"""
Django settings for recetario project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

#encoding:utf-8
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
RUTA_PROYECTO = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gt#or$3h&phaacc)nj!_#=(!a4j=rzqs+kol%@s-3cw$#2(un2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'principal',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'recetario.urls'

WSGI_APPLICATION = 'recetario.wsgi.application'


MEDIA_ROOT = os.path.join(RUTA_PROYECTO,'carga')
MEDIA_URL = '/media/'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'recetario.db',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'
SITE_ID=1

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
    os.path.join(RUTA_PROYECTO,'plantillas'),
)

#configuraciones para enviar mensajes usando gmail
EMAIL_USE_TLS = True
EMAIL_HOST ='smtp.gmail.com'
EMAIL_HOST_USER= 'logoz471@gmail.com'
EMAIL_HOST_PASSWORD = 'hola'
EMAIL_PORT = 587 

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS =(
	os.path.join(RUTA_PROYECTO, 'static'),
)

STATIC_URL = '/static/'
