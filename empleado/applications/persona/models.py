#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria models ORM
from django.db import models
#Base de datos a la cual se hace referencia
from applications.departamento.models import Departamento
#Aplicaciones de terceros()
from ckeditor.fields import RichTextField
#----------------------------------------------------------------------------------------------

#---------------------------------------MODELO 1-----------------------------------------------
# Create your models here.
#Tabla de habilidades 
class Habilidad(models.Model):
    #El id es un campo que se agrega de manera automatica
    habilidad = models.CharField("Habilidad", max_length=100)
    #Clase meta modifica las vistas de Django admin dentro de esta tabla
    class Meta:
        verbose_name="Habilidad"
        verbose_name_plural="Habilidades"
        ordering=["id"]  
    #La funcion __str__ es el mensaje de salida que tendra la tabla Habilidad    
    def __str__(self):
        return str(self.id)+" "+self.habilidad
#----------------------------------------------------------------------------------------------        

#---------------------------------------MODELO 2-----------------------------------------------
#Tabla de empleados
class Empleado(models.Model):
    JOB_CHOICES=(
        ("0","CONTADOR"),
        ("1","ADMINISTRADOR"),
        ("2","ECONOMISTA"),
        ("3","OTRO"),
    )    
    
    first_name = models.CharField("Nombres", max_length=50)
    last_name = models.CharField("Apellidos", max_length=50)
    full_name = models.CharField("Nombre completo", max_length=120,blank=True)
    #Hace referencia a la lista de opciones JOB_CHOICES
    job = models.CharField("Trabajo", max_length=50,choices=JOB_CHOICES)
    #llAVE FORANEA
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    #Imagen
    image = models.ImageField( upload_to="empleado", blank=True,null=True)
    #Relacion de muchos a muchos
    habilidades = models.ManyToManyField("Habilidad")
    #Aplicacion de terceros (ckeditor)
    hoja_vida= RichTextField("Hoja de vida")

    #Clase meta modifica las vistas de Django admin dentro de esta tabla
    class Meta:
        verbose_name="Persona"
        verbose_name_plural="Personas"
        ordering=["id"] 
        #Coincidencias que no deben repetirse 
        unique_together=["first_name","job"]

    #La funcion __str__ es el mensaje de salida que tendra la tabla Empleado 
    def __str__(self):
        return str(self.id)+" "+self.first_name+" "+self.last_name
#---------------------------------------------------------------------------------------------- 