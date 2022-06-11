
from rest_framework import serializers

from .models import Person,Reunion

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=("__all__")
        '''("id",
        "full_name",
        "job",
        "phone",
        "email"
        )'''
#------------------------------------------------------------------------------
#Serializer.Serializer
class PersonaSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    full_name=serializers.CharField()
    job=serializers.CharField()
    email=serializers.EmailField()
    phone=serializers.CharField()
    #
    activo = serializers.BooleanField(default=False,required=False)
    

#------------------------------------
class PersonaSerializer2(serializers.ModelSerializer):
    activo = serializers.BooleanField(default=False,required=False)
    class Meta:
        model=Person
        fields=("__all__")
#---------------------------------------------------------------------
#----------------------------------------------------------
from .models import Hobby
class HobbySerializer(serializers.ModelSerializer):
    class Meta:
        model=Hobby
        fields=("__all__")

#-----------------------------------------------------------------
class PersonaSerializer3(serializers.ModelSerializer):
    hobbies=HobbySerializer(many=True)
    class Meta:
        model=Person
        fields=("id",
        "full_name",
        "job",
        "phone",
        "email",
        "hobbies",
        )
#Serializadores Many to many y foreing key
class ReunionSerializer(serializers.ModelSerializer):
    persona=PersonaSerializer3()
    class Meta:
        model=Reunion
        fields=('id',
        'fecha',
        'hora',
        'asunto',
        'persona',)
#------------------------------------------------------------
