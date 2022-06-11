from rest_framework import serializers

from .models import Empleado

class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Empleado
        fields=("id",
        "first_name",
        "last_name",
        "job",
        "departamento",
        "habilidades",
        )
        
