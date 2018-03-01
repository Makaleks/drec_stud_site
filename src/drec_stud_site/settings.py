"""
Django settings for drec_stud_site project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
from importlib import util

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# TODO: fix for production
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'markdown_deux',
    'social_django',
    'reversion',
    'precise_bbcode',
    'background_task',
    # disable to save media on delete/update
    'django_cleanup',
    'adminsortable2',
    'utils',
    'user',
    'news',
    'note',
    'comment',
    'service',
    'survey',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'drec_stud_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'html')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.static',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.contexts.custom_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'drec_stud_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'drec_stud_site',
        'USER': 'drec_stud_site_admin',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'collected_static')
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
SURVEY_SHEET_ROOT = os.path.join(MEDIA_ROOT, 'surveys')

AUTH_USER_MODEL = 'user.User'

spec = util.spec_from_file_location('setting_additions', os.path.join(PROJECT_ROOT, 'setting_additions.py'))
module = util.module_from_spec(spec)
spec.loader.exec_module(module)
SOCIAL_AUTH_VK_OAUTH2_KEY = module.SOCIAL_AUTH_VK_OAUTH2_KEY
SOCIAL_AUTH_VK_OAUTH2_SECRET = module.SOCIAL_AUTH_VK_OAUTH2_SECRET
SOCIAL_AUTH_VK_OAUTH2_EXTRA_DATA = ['photo_100']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = module.DEBUG

QUESTION_DEFAULT_APPROVED = module.QUESTION_DEFAULT_APPROVED

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = module.SECRET_KEY

# The following key use YANDEX payment mechanics
# You can set up this according to your project (see src/services/templates/):
PAYMENT_TEXT_YANDEX = module.PAYMENT_TEXT_YANDEX
PAYMENT_YANDEX_ENABLE_PHONE = module.PAYMENT_YANDEX_ENABLE_PHONE
PAYMENT_YANDEX_ENABLE_CARD = module.PAYMENT_YANDEX_ENABLE_CARD
PAYMENT_SUCCESS_REDIRECT_YANDEX = module.PAYMENT_SUCCESS_REDIRECT_YANDEX
PAYMENT_SECRET_YANDEX = module.PAYMENT_SECRET_YANDEX
PAYMENT_ACCOUNT_YANDEX = module.PAYMENT_ACCOUNT_YANDEX
IS_EMERGENCY_LOGIN_MODE = module.IS_EMERGENCY_LOGIN_MODE
IS_ID_RECOGNITION_BROKEN_VK = module.IS_ID_RECOGNITION_BROKEN_VK

AUTHENTICATION_BACKENDS = (
    'social_core.backends.vk.VKOAuth2',
    # Uncomment to return #passwordAuth
    'django.contrib.auth.backends.ModelBackend',
)
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['last_name', 'first_name', 'patronymic_name']
# The chain of functions that will bring us to user
SOCIAL_AUTH_PIPELINE = (
    # Get the information we can about the user and return it.
    # On some cases the details are already part of the auth response
    # from the provider, but sometimes this could hit a provider API.
    'social_core.pipeline.social_auth.social_details',
    # Get the social uid from whichever service we're authing thru.
    # The uid is the unique identifier of the given user in the provider.
    'social_core.pipeline.social_auth.social_uid',
    # Verifies that the current auth process is valid within the current
    # project, this is where emails and domains whitelists are applied (if
    # defined).
    'social_core.pipeline.social_auth.auth_allowed',
    # Check that social uid meets requirements
    'user.pipeline.load_user',
    # Checks if the current social-account is already
    # associated in the site.
    'social_core.pipeline.social_auth.social_user',
    # Create the record that associates the social account with the user.
    'social_core.pipeline.social_auth.associate_user',
    # Force login, so you will be reloginned (not done by default)
    #'user.pipeline.force_login',
)
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_SANITIZE_REDIRECTS = False
# So social-auth will not set redirect-url with post
# needs in nginx server settings: 'proxy_set_header Host $host;'
USE_X_FORWARDED_HOST = True

FILE_UPLOAD_PERMISSIONS = 0o644

LOGGING = {
    # The only possible value, I know it`s strange
    'version': 1,
    # Set this True on your own risk
    'disable_existing_loggers': False,
    # Targets: user actions info
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file_user_events': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'user_formatter',
            'filename': os.path.join(PROJECT_ROOT, 'logs/all_events.log'),
        },
        'file_django': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            #'formatter': 'user_formatter',
            'filename': os.path.join(PROJECT_ROOT, 'logs/django_events.log'),
            'formatter': 'verbose',
        },
        'file_payment': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            #'formatter': 'user_formatter',
            'filename': os.path.join(PROJECT_ROOT, 'logs/payment_events.log'),
            'formatter': 'simple',
        },
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'formatters': {
        'user_formatter': {
            # never set default 'user'
            'format': '%(asctime)s: %(levelname)s %(user)s - %(message)s',
            # default formatter includes milliseconds
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'verbose': {
            'format': '####################\n%(asctime)s %(levelname)s %(module)s %(process)d %(thread)d %(message)s\n',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'loggers': {
        'site_events': {
            'handlers': ['file_user_events'],
            'level': 'INFO',
            # don`t pass to handlers of higher level (default: True)
            'propagate': False,
        },
        'django': {
            'handlers': ['console', 'file_django'],
            'level': 'INFO',
            'propagate': True,
        },
        'payment_logs': {
            'handlers': ['file_payment'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
