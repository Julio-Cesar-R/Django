from django.contrib import admin

from .models import Person,Hobby,Reunion

class PersonaAdmin(admin.ModelAdmin):
    #Campos que se mostraran
    list_display=("id",
        "full_name",
        "job",
        "phone",
        "email"
        )
    ordering=["id"]


admin.site.register(Person,PersonaAdmin)
admin.site.register(Hobby)
admin.site.register(Reunion)
