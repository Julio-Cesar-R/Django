from django.contrib import admin

from .models import Categoria, Libro

class CategoriaAdmin(admin.ModelAdmin):
    #Campos que se mostraran
    list_display=("id",
    "nombre")
    #Filtros de busqueda
    ordering=("id",)

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Libro)
