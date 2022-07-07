from dataclasses import fields
from importlib import import_module
from rest_framework import serializers,pagination

from .models import Demostracion

class DemostracionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Demostracion
        fields=("__all__")
class DemostracionAPIcreate(serializers.ModelSerializer):
    class Meta:
        model=Demostracion
        fields=("__all__")