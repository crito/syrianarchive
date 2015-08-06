from syrianarchive.site_settings import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2',$
        'NAME': 'syarch_db_name',
        'USER': 'syarch_db_user',
        'PASSWORD': 'very#good#password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

SECRET_KEY = 'a_secret_key'

#for production
DEBUG = False

#for development
DEBUG = True
