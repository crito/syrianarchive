from os.path import dirname, join, realpath

from django.conf.global_settings import *


BASE_PATH = realpath(join(dirname(__file__), '..'))

ADMINS = ()
MANAGERS = ()

ALLOWED_HOSTS = ()
ADMIN_MEDIA_PREFIX = '/static/admin/'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'modeltranslation',
    #'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_summernote',
    'rosetta',
    'database',
    'homepage',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'solid_i18n.middleware.SolidLocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_ROOT = BASE_PATH + '/media/'
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = join(BASE_PATH, 'static-collected')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(BASE_PATH, 'static'),
)

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
TEMPLATE_DIRS = (
    join(BASE_PATH, 'templates'),
)


SUMMERNOTE_CONFIG = {
    # Using SummernoteWidget - iframe mode
    'iframe': False,  # or set False to use SummernoteInplaceWidget - no iframe mode

    # Using Summernote Air-mode
    'airMode': False,

    # Use native HTML tags (`<b>`, `<i>`, ...) instead of style attributes
    # (Firefox, Chrome only)
    'styleWithTags': True,

    # Change editor size
    'width': '100%',
    'height': '480',

    # Customize toolbar buttons
    'toolbar': [
        ['style', ['style']],
        ['style', ['bold', 'italic', 'underline', 'clear']],
        ['para', ['ul', 'ol']],
        ['insert', ['link']],
    ],

}




















ROOT_URLCONF = 'syrianarchive.urls'

WSGI_APPLICATION = 'syrianarchive.wsgi.application'

TIME_ZONE = 'UTC'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# Path to locale folder
LOCALE_PATHS = (
   BASE_PATH + '/locale',
)

# The language your website is starting in
LANGUAGE_CODE = 'en'

# The languages you are supporting
LANGUAGES = (
    ('en', 'English'),   # You need to include your LANGUAGE_CODE language
    ('ar', 'Arabic'),
)

# Use internationalization
USE_I18N = True

# Use localization
USE_L10N = True

# Optional. If you want to use redirects, set this to True
SOLID_I18N_USE_REDIRECTS = False

SOLID_I18N_DEFAULT_PREFIX_REDIRECT = True