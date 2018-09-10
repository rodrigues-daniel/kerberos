"""
Django settings for kerberos project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, seeim
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hq4#1e&7@6ql1b$649r3$!t8efzjg31=ua#dt3z!1brajk3bsk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.24.0.222','127.0.0.1']




AUTH_LDAP_SERVER_URI = "ldaps://prd-ad01.tce.govrn:636"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'kerberosadm.apps.KerberosadmConfig',
    'permissoes.apps.PermissoesConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
]

ROOT_URLCONF = 'kerberos.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['kerberos/templates'],
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

WSGI_APPLICATION = 'kerberos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

try:
    from kerberos import local_settings
except ImportError:
    pass


DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': local_settings.NAME,
        'HOST': local_settings.HOST,
        'PORT': local_settings.PORT,
        'USER': local_settings.USER,
        'PASSWORD': local_settings.PASSWORD,
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            },
    }
}


'''
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType
'''

AUTHENTICATION_BACKENDS = (
    'django_python3_ldap.auth.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
    'django.contrib.auth.backends.RemoteUserBackend',
)

# The URL of the LDAP server.
LDAP_AUTH_URL = "ldap://prd-ad01.tce.govrn:389"

# Initiate TLS on connection.
LDAP_AUTH_USE_TLS = False


# The LDAP search base for looking up users.
LDAP_AUTH_SEARCH_BASE = "dc=tce,dc=govrn"
LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"

LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory"

LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "TCE"

LDAP_AUTH_CONNECTION_USERNAME = ""
LDAP_AUTH_CONNECTION_PASSWORD = ""



LDAP_AUTH_FORMAT_USERNAME = "django_python3_ldap.utils.format_username_active_directory_principal"
LDAP_AUTH_ACTIVE_DIRECTORY_DOMAIN = "tce.govrn"



LDAP_AUTH_USER_FIELDS = {
    "username": "sAMAccountName",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

LDAP_AUTH_OBJECT_CLASS = "user"

LDAP_AUTH_CLEAN_USER_DATA = "django_python3_ldap.utils.clean_user_data"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django_python3_ldap": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Recife'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
