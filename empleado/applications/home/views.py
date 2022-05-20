from django.shortcuts import render

# Create your views here.

#vistas genericas

from django.views.generic import TemplateView

class Pruebaview(TemplateView):
    template_name= "home/prueba.html"