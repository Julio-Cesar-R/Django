from django.shortcuts import render
from django.views.generic import ListView,CreateView
from rest_framework.generics import ListAPIView,CreateAPIView

from .models import Person

#---------------------------------------------------------------------------
#----------------------------LIST VIEW PERSONAS------------------------
from .serializers import PersonSerializer
class PersonaListView(ListView):
    template_name = "persona/lista_personas.html"
    context_object_name="personas"

    def get_queryset(self):
        
        return Person.objects.all()
#-------------------------------------------------------------------------
#Serializador
class PersonlistAPIview(ListAPIView):
    #formato json
    serializer_class=PersonSerializer
    def get_queryset(self):
        
        return Person.objects.all()
    #serializar




#---------------------------------------------------------------------------

#---------------LISTVIEW POR PK Detail view---------------------------------------------

class PersonapkListView(ListView):
    template_name = "persona/listapk.html"
    context_object_name="empleado_pk"
    
    #Funcion que recibe informacion mediante la URL
    def get_queryset(self):
        #Variable que almacena el valor ingresador en la URL
        #Recibe un parametro mediante una url
        primary=self.kwargs["pk"]
        #Compara la informacion recibida en la url con la de la base
        lista=Person.objects.filter(id=primary)
        return lista
#---------------------------------------------------------------------------
#Serializador
from rest_framework.generics import RetrieveAPIView
class PersonpkAPIview(RetrieveAPIView):
    #formato json
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
#------------------------------------------------------

#-----------------CREATE VIEW--------------------------
from django.urls import reverse_lazy
from .forms import PersonForm
class PersonAddCreateView(CreateView):
    model = Person
    template_name = "persona/person_add.html"
    form_class= PersonForm
    success_url=reverse_lazy("persona_app:add_persona")
#-------------------------------------------------------------
#Serializer    
class PersonAPIcreate(CreateAPIView):
    serializer_class=PersonSerializer


#----------------------VISTA UPDATE-----------------------------------
from .forms import PersonForm
from django.views.generic import UpdateView
class PersonUpdateView(UpdateView):
    model = Person
    template_name = "persona/update_person.html"
    form_class=PersonForm
    success_url=reverse_lazy("persona_app:persona_lista")
#----------------------------------------------------------
#Serializer
from rest_framework.generics import UpdateAPIView,RetrieveUpdateAPIView
class PersonAPIUpdate(UpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
#----------------------------------------------------------------------
#Mejor opcion de update
class PersonAPIUpdateretrieve(RetrieveUpdateAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
#----------------------------------------------------------------------------------------

#------------------DELETE-----------------------------------------------------
from django.views.generic import DeleteView

class PersonDeleteView(DeleteView):
    model = Person
    template_name = "persona/delete_persona.html"
    success_url=reverse_lazy("persona_app:persona_lista")
#---------------------------------------------------------------------
#serializer
from rest_framework.generics import DestroyAPIView
class PersonAPIDelete(DestroyAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
#Mejor opcion de Delete
from rest_framework.generics import RetrieveDestroyAPIView
class PersonAPIDeleteretrieve(RetrieveDestroyAPIView):
    serializer_class=PersonSerializer
    queryset=Person.objects.all()
#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#------------SERIALIZER.SERIALIZER------------------------------------
from .serializers import PersonaSerializer

#Serializador
class PersonlistAPIserializer(ListAPIView):
    #formato json
    serializer_class=PersonaSerializer
    def get_queryset(self):
        
        return Person.objects.order_by("id")
    #serializar

#-----------------------------------------------------------
from .serializers import PersonaSerializer2
class PersonlistAPIserializer2(ListAPIView):
    #formato json
    serializer_class=PersonaSerializer2
    def get_queryset(self):
        
        return Person.objects.order_by("id")

#---------------------------------------------------------------------
#Serializadores Many to many y foreing key
from .serializers import ReunionSerializer
from .models import Reunion

class ReunionApi(ListAPIView):
    #formato json
    serializer_class=ReunionSerializer
    def get_queryset(self):
        
        return Reunion.objects.order_by("id")
#-----------------------------------------------
from .serializers import PersonaSerializer3
class PersonlistAPIserializer3(ListAPIView):
    #formato json
    serializer_class=PersonaSerializer3
    def get_queryset(self):
        
        return Person.objects.order_by("id")
