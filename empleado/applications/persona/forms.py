
from tkinter import Widget
from django import forms
from .models import Empleado

class PersonForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'first_name',
            'last_name',
            'job',
            'departamento',
            'image',
            'habilidades',
            'hoja_vida',
            )
        widgets={
            "habilidades" :forms.CheckboxSelectMultiple()
        }
