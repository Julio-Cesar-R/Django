from django.shortcuts import render
from django.views.generic import ListViewst
from .models import Person


class PersonaListView(ListView):
    model = Person
    template_name = "TEMPLATE_NAME"







