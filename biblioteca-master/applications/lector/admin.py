from django.contrib import admin

from .models import Lector, Prestamo


class PrestamoAdmin(admin.ModelAdmin):
    #Campos que se mostraran
    list_display=("id",
    "lector",
    "libro")
    #Filtros de busqueda
    ordering=("id",)

admin.site.register(Prestamo,PrestamoAdmin)

admin.site.register(Lector)
