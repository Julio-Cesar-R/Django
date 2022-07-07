#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria models ORM
from django.db import models

#----------------------------------------------------------------------------------------------
# Create your models here.
#Tabla de empleados
class Demostracion(models.Model):
    
    
    dato1 = models.CharField("Dato1", max_length=50)
    dato2 = models.CharField("Dato2", max_length=50)
    dato3= models.CharField("Dato3", max_length=120,blank=True)
    


    #Clase meta modifica las vistas de Django admin dentro de esta tabla
    class Meta:
        verbose_name="Demostracion"
        verbose_name_plural="Demostraciones"
        ordering=["id"] 
        #Coincidencias que no deben repetirse 
        

    #La funcion __str__ es el mensaje de salida que tendra la tabla Empleado 
    def __str__(self):
        return str(self.id)+" "+self.dato1+" "+self.dato2+" "+self.dato3
#---------------------------------------------------------------------------------------------- 
