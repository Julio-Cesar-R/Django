#---------------------------------------LIBRERIAS---------------------------------------------
#Configuracion de paths con Unipath

#---------------------------------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#-----------path configurado con unipath
from django.core.exceptions import ImproperlyConfigured
import json

from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)


with open("secret.json") as f:
    secret = json.loads(f.read())

def get_secret(secret_name, secrets=secret):
    try:
        return secrets[secret_name]
    except:
        msg = "la variable %s no existe" % secret_name
        raise ImproperlyConfigured(msg)

SECRET_KEY = get_secret('SECRET_KEY')
#---------------------------------------APLICACIONES---------------------------------------------
# Application definition
DJANGO_APPS = (
    #Aplicaciones por default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
    
LOCAL_APPS=(
    "app.app1",
    "app.home",
)
THIRD_PARTY_APPS=(
    "ckeditor",
    "rest_framework")

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
#---------------------------------------------------------------------------------------------

#---------------------------------------MIDDLEWARE--------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#---------------------------------------------------------------------------------------------

#---------------------------------------URL-CONFIG--------------------------------------------
#Url principal
ROOT_URLCONF = 'config.urls'
#---------------------------------------------------------------------------------------------

#---------------------------------------TEMPLATES--------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #para que reconozca la carpeta template en la estructura instalar unipath
        # Ubicacion de los templates "child("templates")],"
        'DIRS': [BASE_DIR.child("templates")],
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
#---------------------------------------------------------------------------------------------

#------------------------------------------WSGI_APP--------------------------------------------
WSGI_APPLICATION = 'config.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
#---------------------------------------------------------------------------------------------

#------------------------------------------WSGI_APP--------------------------------------------
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
#---------------------------------------------------------------------------------------------

#------------------------------------------IDIOMA--------------------------------------------
# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
#---------------------------------------------------------------------------------------------
