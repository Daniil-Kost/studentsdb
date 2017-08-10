"""
Django settings for studentsdb project.

Generated by 'django-admin startproject' using Django 1.10.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os
import email

import json

from django.core.exceptions import ImproperlyConfigured

import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '91i_4a-y_@q7i9*yxzzw^+xnh94h6n^j$2)o99cb27-t@ix@@w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'registration',
    'social.apps.django_app.default',
    'students',
    'stud_auth',
    'studentsdb',
	]

MIDDLEWARE_CLASSES = [
    'studentsdb.middleware.RequestTimeMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
	]

ROOT_URLCONF = 'studentsdb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.core.context_processors.request",
                "studentsdb.context_processors.students_proc",
        "students.context_processors.groups_processor",
        "students.context_processors.lang_processor",
         "students.context_processors.style_processor",
         "students.context_processors.background_processor",
         "students.context_processors.color_text_processor",
         "students.context_processors.link_processor",
         "students.context_processors.focus_processor",
        "social.apps.django_app.context_processors.backends",
        "social.apps.django_app.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = 'studentsdb.wsgi.application'

#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.mysql',
 #       'HOST': 'localhost',
 #       'USER': 'students_db_user',
 #       'PASSWORD': '12345678',
 #       'NAME': 'students_db',
 #   }
#}

# Parse database configuration from $DATABASE_URL
DATABASES = {'default': dj_database_url.parse('postgres://...')}
HEROKU_POSTGRESQL_ONYX_URL = 'postgres://...'

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Enable Connection Pooling
DATABASES['default']['ENGINE'] = 'django_postgrespool'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'

STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    )

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

PORTAL_URL = 'http://localhost:8000'

MEDIA_URL ='/media/'

MEDIA_ROOT =os.path.join(BASE_DIR, '..', 'media')



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

ADMIN_EMAIL = 'lemk@ukr.net'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '465'
EMAIL_HOST_USER = 'studentsdb1111@gmail.com'
EMAIL_HOST_PASSWORD = 'kynhbquucgwxpsdp'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

SITE_ID = 1
#SERVER_EMAIL = "lemk1997@gmail.com"
#DEFAULT_FROM_EMAIL = "admin@studentsdb.uk.to"
#MANAGERS = [('admin','lemk1997@gmail.com')]
ADMINS = (
    ('admin', 'lemk1997@gmail.com'),
    ('lemk', 'lemk@ukr.net'),
)


#registration
REGISTRATION_OPEN = True

LOGIN_URL = 'users:auth_login'
LOGOUT_URL = 'users:auth_logout'

AUTHENTICATION_BACKENDS = (
	'social.backends.facebook.FacebookOAuth2',
	'social.backends.google.GoogleOAuth2',
	'social.backends.google.GoogleOpenId',
    'social.backends.github.GithubOAuth2',
    'social.backends.twitter.TwitterOAuth',
	'django.contrib.auth.backends.ModelBackend',
	)

#Facebook keys
SOCIAL_AUTH_FACEBOOK_KEY = '414276622259701'
SOCIAL_AUTH_FACEBOOK_SECRET = '6fd14960af6473dc246c5cd22a3362ae'

# Google Keys
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '340441235543-jhhbmg5cn4hfst0eaca4djfrimb4tg9m.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'uB1h1COTNY9lt8_oGPeNs8OX'

#GitHub Keys
SOCIAL_AUTH_GITHUB_KEY = '1d0d4bb26966159e9534'
SOCIAL_AUTH_GITHUB_SECRET = '1c2e16f3e1d670502ea5d8d0d3f8c6344b3bdf63'

#Twitter Keys
SOCIAL_AUTH_TWITTER_KEY = 'CjdhI6fCY64kItX6CqKfjZplt'
SOCIAL_AUTH_TWITTER_SECRET = 'iK3lruIzn7YHQL93gKcXGpqfclaye2S3C8fo3Npj4x3HjqRA46'


SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

# Google OAuth2 (google-oauth2)
SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

# Google+ SignIn (google-plus)
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
'https://www.googleapis.com/auth/plus.login',
'https://www.googleapis.com/auth/userinfo.email',
'https://www.googleapis.com/auth/userinfo.profile'
]

SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True
SOCIAL_AUTH_GOOGLE_PLUS_USE_DEPRECATED_API = True

CRISPY_TEMPLATE_PACK = 'bootstrap3'

#logging
LOG_FILE = os.path.join(BASE_DIR, 'studentsdb.log')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s: %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': LOG_FILE,
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': True,
            'level': 'INFO',
        },
        'students.signals': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'students.views.contact_admin': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        }
    }
}