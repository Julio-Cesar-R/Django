from django.shortcuts import render

# Create your views here.

#vistas genericas

from django.views.generic import TemplateView,ListView,CreateView

#Base de datos
from .models import Prueba 
#templateview Muesta un archivo html
#Listview Se utiliza para mostrar un listado (base de datos)
#Create view
class Pruebaview(TemplateView):
    template_name= "home/prueba.html"

class Resumenfoundationview(TemplateView):
    template_name= "home/resumenfoundation.html"


class PruebaListView(ListView):
    #Sustituye la base
    queryset=["0","1","10","20"]
    #Template al que se envia la informacion
    template_name = "home/lista.html"
    #listanumeros es la variable que se envia al template
    context_object_name="listanumeros"


class ListapruebaListView(ListView):
    
    template_name = "home/listaprueba.html"
    model = Prueba
    context_object_name= "lista"

#----------------------Vista
#Importamos el form desde forms.py
from .forms import PruebaForm
#Vista com con model form
class PruebaCreateView(CreateView):
    #Modelo
    model = Prueba
    #Template
    template_name = "home/pruebacreate.html"
    #Informacion que se enviara al html
    form_class=PruebaForm
    #redirecciona a la pagina de inicio
    success_url="/"

