from django.contrib import admin

from .models import Autor
# Register your models here.
class AutorAdmin(admin.ModelAdmin):
    #Campos que se mostraran
    list_display=("id",
    "nombres",
    "apellidos",
    "nacionalidad",
    "edad")


    #Filtros de busqueda
    ordering=("id",)

admin.site.register(Autor,AutorAdmin)
