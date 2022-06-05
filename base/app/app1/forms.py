import imp
from tkinter import Widget
from django import forms
from .models import Demostracion

class DemostracionForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Demostracion
        fields = (
            'dato1',
            'dato2',
            'dato3',
            
            )

