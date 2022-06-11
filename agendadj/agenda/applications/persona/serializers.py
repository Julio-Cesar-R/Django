
from rest_framework import serializers,pagination



from .models import Person,Reunion

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=("__all__")
       
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


#---------------------MANY TO MANY Y FOREING KEY
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
#SERIALIZER CON METODO
class MethodSerializer(serializers.ModelSerializer):
    hora_fecha=serializers.SerializerMethodField()
    
    class Meta:
        model=Reunion
        fields=('id',
        'fecha',
        'hora',
        'asunto',
        'persona',
        'hora_fecha')
    
    def get_hora_fecha(self,obj):
        return str(obj.hora)+"-"+str(obj.fecha)

#-----Hyperlink serializer
class ReunionSerializerlink(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model=Reunion
        fields=('id',
        'fecha',
        'hora',
        'asunto',
        'persona',)
        extra_kwargs={
            'persona':{'view_name': 'persona_app:api_pk_empleados', 'lookup_field':'pk'}
        }
#---------------------------------------------------------------------------
#Paginacion
class PersonSerializer2(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields=("__all__")

class PersonPagination(pagination.PageNumberPagination):
    page_size=5
    max_page_size=100
#------------------------------------------------------------------
#Metodos en manager
class ReunionesJobSerializer(serializers.Serializer):
    persona__job = serializers.CharField()
    cantidad = serializers.IntegerField()

