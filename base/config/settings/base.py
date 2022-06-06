#---------------------------------------LIBRERIAS---------------------------------------------
#Configuracion de paths con Unipath
from pathlib import Path
#---------------------------------------------------------------------------------------------

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#-----------path configurado con unipath
from unipath import Path
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u5h4i@k8zl$24!dhx)=22c)ue@5y%$pg)hpr&@#*wt6rcjx0)f'

#---------------------------------------APLICACIONES---------------------------------------------
# Application definition
INSTALLED_APPS = [
    #Aplicaciones por default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #Apps de terceros
    "ckeditor",

    #local apps
    "app.app1",
    "app.home",
]
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
