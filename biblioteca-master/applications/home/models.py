#-------------MODELOS ABSTRACTOS Y METADATOS-----------------------


from enum import unique
from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    # TODO: Define fields here
    full_name = models.CharField("Nombres", max_length=50)
    pais = models.CharField("Pais", max_length=50)
    pasaporte = models.CharField("Pasaporte", max_length=50)
    edad = models.PositiveIntegerField()
    apelativo = models.CharField("Apelativo", max_length=50)
    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        #Nombre que se mostrara en la base en postgres
        db_table="persona"
        unique_together=["pais","apelativo"]
        constraints=[
            models.CheckConstraint(check=models.Q(edad__gte=18),name="edad_mayor_18")
        ]

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name
    #Modelo abstracto
    abstract=True

class Empleado(Persona):
    trabajo = models.CharField("Trabajo", max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        #Nombre que se mostrara en la base en postgres
        db_table="empleado"


    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name

class Cliente(Persona):
    email = models.CharField("E-mail", max_length=50)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        #Nombre que se mostrara en la base en postgres
        db_table="cliente"


    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name