
from django import forms
from .models import Prueba

#mf en djaneiro
# Model Form
class PruebaForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Prueba
        #fields = ('__all__')
        fields=("titulo",
                "subtitulo",
                "cantidad")
       
       #Personalizar campos en el formulario
       #placeholder
       #Investigar django widgets
        widgets={"titulo": forms.TextInput(
            attrs={
                "placeholder":"Ingrese el titulo"

            }
        ),

        "subtitulo":forms.TextInput(
            attrs={
               "placeholder":"Ingrese el subtitulo" 
            }
        ),

        "cantidad":forms.NumberInput(
            attrs={
               "placeholder":"Ingrese la cantidad" 
            }
        )

        }

    def clean_cantidad(self):
        #recupera la informacion ingresada en el formulario
        cantidad=self.cleaned_data["cantidad"]
        if cantidad<10:
            raise forms.ValidationError("Ingrese un numero mayor a 10")

        return cantidad