#---------------------------------------LIBRERIAS---------------------------------------------
#importar todo lo que tenga archivo base.py
from .base import *
#---------------------------------------------------------------------------------------------

#--------------------------------CONFIGURACION/BASE DE DATOS-----------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
ALLOWED_HOSTS = []
#---------------------------------------BASE DE DATOS-------------------------------------------


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': get_secret('DB_NAME'),
        'USER': get_secret('USER'),
        'PASSWORD': get_secret('PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

#Archivos estaticos
STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child("static")]
#----------------------------------------------------------------------------------------------
#Archivos multimedia (Carpeta media)
media_url="/media/"
MEDIA_ROOT=BASE_DIR.child("media")