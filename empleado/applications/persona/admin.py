#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria para registrar los modelos de la aplicacion
from django.contrib import admin
#Modelos del archivo models.py
from .models import Empleado,Habilidad
#---------------------------------------------------------------------------------------------

#----------------------------------------REGISTRO---------------------------------------------
#Clase que modifica Django-admin y como se muestran los datos
class EmpleadoAdmin(admin.ModelAdmin):
    #Campos que se mostraran
    list_display=("first_name",
    "last_name",
    "departamento",
    "job",
    #Campo añadido donde se concatena nombre y apellido
    "full_name")

    #Funcion que concatena nommbre y apellido, con el nombre del campo
    def full_name(self,obj):
        return obj.first_name+" "+obj.last_name


    #Filtros de busqueda
    search_fields=("first_name",)
    list_filter=("departamento","job","habilidades")
    filter_horizontal=("habilidades",)
#---------------------------------------------------------------------------------------------
#----------------------------------------REGISTRO---------------------------------------------
# Register your models here.
#Registro de la tabla Habilidad
admin.site.register(Habilidad)
admin.site.register(Empleado,EmpleadoAdmin)
#---------------------------------------------------------------------------------------------
