"""
Django settings for django_server project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from django.core.exceptions import ImproperlyConfigured
from pathlib import Path
import os
import json

with open("secrets.json") as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_secret("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # pip
    ## DRF
    'rest_framework',
    ## DRF - token auth
    'rest_framework.authtoken',
    ## rest_auth
    'django.contrib.sites',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    ## CORS
    'corsheaders',
    ## yasg
    'drf_yasg',
    ## django_storages
    'storages',

    # original
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # our apps
    'accounts',
    'photos',
    'diaries',
    'babies',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'babble',
        'USER': 'dragon',
        'PASSWORD': get_secret('DB_PASSWORD'),
        'HOST': 'j3a310.p.ssafy.io',
        # 'NAME': 'babble',
        # 'USER': 'root',
        # 'PASSWORD': '',
        # 'HOST': '',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ko-KR'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# static
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

AUTH_USER_MODEL = 'accounts.User'

SITE_ID = 1

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ]
}

CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = []


DEFAULT_FILE_STORAGE = 'django_server.storages.MediaStorage'
STATICFILES_STORAGE = 'django_server.storages.StaticStorage'

MEDIAFILES_LOCATION = 'media'
STATICFILES_LOCATION = 'static'

# Make sure delete from here before commit
AWS_REGION = get_secret('AWS')['REGION']
AWS_STORAGE_BUCKET_NAME = get_secret('AWS')['BUCKET_NAME']
AWS_ACCESS_KEY_ID = get_secret('AWS')['ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = get_secret('AWS')['SECRET_KEY']
AWS_STORAGE_BUCKET_NAME = 'babble-bucket'

AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME