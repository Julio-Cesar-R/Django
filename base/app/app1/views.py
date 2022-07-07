#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from .models import Demostracion
# Create your views here.
#IMPORTAR FORMS
from .forms import DemostracionForm
#IMPORTA VISTAS GENERICAS
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView,FormView
#Importa redireccionamiento de urls
from django.urls import reverse_lazy

#-----------------------VISTAS------------------------------------
class DemostracionCreateView(CreateView):
    #Modelo
    model = Demostracion
    #Template
    template_name = "app1/demostracion.html"
    form_class= DemostracionForm
    #Campos
    #fields=["first_name","last_name","job","departamento","departamento","image","habilidades","hoja_vida"]
    #fields=("__all__") 
    success_url=reverse_lazy("app1_app:create_demostracion")
#--------------------------------------------------------------------------------------------
#--------------------------------SERIALIZERS VIEWS----------------------------------
from rest_framework.generics import ListAPIView,CreateAPIView
from .serializers import DemostracionSerializer,DemostracionAPIcreate

class DemostracionAPIView(ListAPIView):
    serializer_class=DemostracionSerializer
    def get_queryset(self):
        queryset = Demostracion.objects.filter(dato1="kaiser")
        return queryset

class DemostracionAPICreatee(CreateAPIView):
    serializer_class=DemostracionAPIcreate