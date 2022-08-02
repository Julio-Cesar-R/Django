
from django.db import models
from django.db.models import Q,Avg,Count,Sum
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    """ managers para el modelo Prestamos """

    def buscar_todo(self):
        '''
        Funcion que retorna todos los prestamos
        '''
        resultado=self.all()

        for p in resultado:
            print(p.lector)
            print(p.libro)
            print(p.libro.categoria)
            
            
        
        return resultado



    def libro_promedios_edades(self,libro):
        '''
        Funcion que retorna el promedio de edades de los lectores que
        realizaron un prestamo de un libro en particular

        '''
        resultado = self.filter(
            
            libro__id__contains=libro
        ).aggregate(
            promedio_edad=Avg("lector__edad"),
            suma_edad=Sum("lector__edad")
        )
        

        return resultado

    def num_lib_prestados(self):
        '''
        Funcion que retorna la cantidad de prestamos realizados por libro
        "values=Group by"
        '''
        resultado= self.values(
            "libro"
        ).annotate(
            num_prestados=Count("libro"),
            libro_titulo=Lower("libro__titulo"),
        ).order_by("-num_prestados")#Order by de manera descendente
        print(type(resultado))
        for r in resultado:
            print("============")
            print(r, r["num_prestados"]) 
    
            
        
        return resultado
            