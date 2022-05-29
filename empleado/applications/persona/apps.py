#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria appconfig
from django.apps import AppConfig
#----------------------------------------------------------------------------------------------

#---------------------------------------CONFIGURACION------------------------------------------
#Configuracion de la APP
class PersonaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.persona'
#----------------------------------------------------------------------------------------------