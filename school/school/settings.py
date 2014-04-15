"""
Django settings for school project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from registration_defaults.settings import *

SETTINGS_DIR = os.path.dirname(__file__)
BASE_DIR = os.path.dirname(SETTINGS_DIR)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_PATH, 'assets'),
)

# TinyMCE settings
STATIC_DIR = os.path.join(PROJECT_PATH, 'static')
STATIC_JS_DIR = os.path.join(STATIC_DIR, "js")
TINYMCE_JS_ROOT = os.path.join(STATIC_JS_DIR, "tiny_mce")
TINYMCE_JS_URL = os.path.join(TINYMCE_JS_ROOT, "tiny_mce.min.js")
#TINYMCE_JS_URL = '/static/js/tinymce/tiny_mce.min.js'
# TINYMCE_JS_ROOT = os.path.join(PROJECT_PATH, '/static/js/tiny_mce')
TINYMCE_DEFAULT_CONFIG = {
    'plugins': "table,paste,searchreplace",
    'theme': "advanced",
}
TINYMCE_SPELLCHECKER = False
TINYMCE_COMPRESSOR = False

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-a$w*$98+95uq$j&h)wz1mmm4u-j4akt+0#oap%9p9^z76q(t#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

AUTH_PROFILE_MODULE = 'admissions.UserProfile'

# Application definition

INSTALLED_APPS = (
    #'django_admin_bootstrapped.bootstrap3',
    #'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'admissions',
    'crispy_forms',
    'haystack',
    'django_extensions',
    'sorl.thumbnail',
    'tinymce',
    'newsletter',
    'forms_builder.forms',
    'tastypie', #can be removed, moving to 'rest_framework'
    'rest_framework',
    #'south',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'school.urls'

WSGI_APPLICATION = 'school.wsgi.application'

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False




TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DIRS = (TEMPLATE_PATH,)  #REGISTRATION_TEMPLATE_DIR,

# Absolute path to the media directory
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

MEDIA_URL = '/media/'

LOGIN_URL = '/accounts/login/'

ACCOUNT_ACTIVATION_DAYS = 2

# The URL where requests are redirected after login when the contrib.auth.login view gets no next parameter.
LOGIN_REDIRECT_URL = '/'

#####  django-contact-form related settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'django.sandeep.lakshmipathy'
EMAIL_HOST_PASSWORD = 'django123'

#By default, the From: header of all emails sent by django-contact-form will be whatever email address is specified in DEFAULT_FROM_EMAIL
DEFAULT_FROM_EMAIL = 'django.sandeep.lakshmipathy@gmail.com'

#The recipient list for emails sent by django-contact-form will be the email addresses
MANAGERS = [('Sandeep','sandeepl79@gmail.com')]

FISTURE_DIRS = (os.path.join(PROJECT_PATH, 'fixtures'), )






# Haystack / solr related settings
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr'
        # ...or for multicore...
        # 'URL': 'http://127.0.0.1:8983/solr/mysite',
    },
}


# Newsletter options
NEWSLETTER_CONFIRM_EMAIL = True
# Using django-tinymce
NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"


REST_FRAMEWORK = {
    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.HyperlinkedModelSerializer',

    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #]
}