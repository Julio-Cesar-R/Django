from msilib import make_id
from tabnanny import verbose
from unicodedata import name
from django.db import models

# Create your models here.

class Departamento(models.Model):
    name = models.CharField("Nombre",max_length=50)
    shortname = models.CharField("Nombre corto", max_length=20,unique=True)
    status = models.BooleanField("Anulado",default=False)

    class Meta:
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"
        ordering=["id"]
        unique_together=["name","shortname"]

    
    def __str__(self):
        return self.name
