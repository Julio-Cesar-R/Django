from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Person
        fields=("id",
        "full_name",
        "job",
        "phone",
        "email"
        )