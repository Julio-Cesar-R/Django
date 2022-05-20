from django.apps import AppConfig


class DepartamentoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    #Agregar applications.
    name = 'applications.departamento'
