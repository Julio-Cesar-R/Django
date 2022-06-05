#---------------------------------------LIBRERIAS---------------------------------------------
#importar todo lo que tenga archivo base.py
from .base import *
#---------------------------------------------------------------------------------------------

#--------------------------------CONFIGURACION/BASE DE DATOS-----------------------------------
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#---------------------------------------BASE DE DATOS-------------------------------------------
DATABASES = {
    'default': {
        #Conexion a base de datos en postgresql con psycopg2
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "dbempleado",
        'USER': "kaiser",
        'PASSWORD': "admin",
        'HOST': "localhost",
        'PORT': "5432",
        
        
    }
}

#Archivos estaticos
STATIC_URL = '/static/'
STATICFILES_DIRS=[BASE_DIR.child("static")]
#----------------------------------------------------------------------------------------------
#Archivos multimedia (Carpeta media)
media_url="/media/"
MEDIA_ROOT=BASE_DIR.child("media")