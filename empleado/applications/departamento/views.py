from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

class Departamentoview(TemplateView):
    template_name= "departamento/departamento.html"