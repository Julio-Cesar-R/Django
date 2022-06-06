#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS Demostracion
from .models import Demostracion
# Create your views here.
#IMPORTAR FORMS
from .forms import DemostracionForm
#IMPORTA VISTAS GENERICAS
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
#Importa redireccionamiento de urls
from django.urls import reverse_lazy

class DemostracionCreateView(CreateView):
    #Modelo
    model = Demostracion
    #Template
    template_name = "app1/demostracion.html"
    form_class= DemostracionForm
    #Campos
    #fields=["first_name","last_name","job","departamento","departamento","image","habilidades","hoja_vida"]
    #fields=("__all__")
#------------------------------------------------------------------------------------------
 #REDIRECCIONAMIENTO NO RECOMENDADO   
    #Pagina que rediccionara cuando la vista cumpla su cometido "."= el mismo template
    #Url no template
    #success_url= "/success"
#------------------------------------------------------------------------------------------    
#REDIRECCIONAMIENTO CON DJANGO 
# libreria reverse_lazy
#   persona_app (etiqueta de las urls) correcto (name de la url)   
    success_url=reverse_lazy("app1_app:create_demostracion")

    