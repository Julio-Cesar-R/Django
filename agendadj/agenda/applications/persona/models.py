#
from model_utils.models import TimeStampedModel

#
from django.db import models

from .manager import ReunionManager
#----------------------------------------------------------------------
class Hobby(TimeStampedModel):
    '''Pasariempos'''

    pasatiempo = models.CharField("Pasatiempo", max_length=50)

    class Meta:
        verbose_name = 'Hobby'
        verbose_name_plural = 'Hobbies'
        ordering=["id"] 
        
    
    def __str__(self):
        return self.pasatiempo    
#---------------------------------------------------------------------------------------
class Person(TimeStampedModel):
    """  Modelo para registrar personas de una agenda  """
    

    full_name = models.CharField(
        'Nombres', 
        max_length=50,
    )
    job = models.CharField(
        'Trabajo', 
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        blank=True, 
        null=True
    )
    phone = models.CharField(
        'telefono',
        max_length=15,
        blank=True,
    )
    hobbies=models.ManyToManyField(Hobby)


    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        ordering=["id"] 
        
    
    def __str__(self):
        return self.full_name
#---------------------------------------------------------------------
class Reunion(TimeStampedModel):
    
    persona=models.ForeignKey(
        Person,
        on_delete=models.CASCADE
    )
    fecha = models.DateField()
    hora = models.TimeField()
    asunto = models.CharField(
        "Asunto de reunion",
         max_length=50)
    objects = ReunionManager()   
    class Meta:
        verbose_name = 'Reunion'
        verbose_name_plural = 'Reuniones'
        
    
    def __str__(self):
        return self.asunto



