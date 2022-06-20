import datetime

from django.db import models

from django.db.models import Q
from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    """ managers para el modelo autor """

    def listar_libros(self, kword):
        '''
        1-Lista los libros que coincidan con la "kword"
        2-Que se encuentren en un rango de fechas determinado por "fecha__range"
        '''
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2000-01-01', '2030-01-01')
        )
        
        return resultado
    
    def listar_libros_trg(self, kword):
        
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,
            )
            return resultado
        else:
            return self.all()[:10]

    
    def listar_libros2(self, kword, fecha1, fecha2):
        '''
        Funcion que recibe 3 parametros
        kword : Titulo del libro
        fecha1: Rango de fecha inicial
        fecha2: Rango de fecha limite

        return: -Coincidencia de nombres
                -Coincidencia entre rango de fechas
        '''
        #Se le da un foormato de fecha a los parametros recibidos en el formulario
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
        
        #Consulta a la base de datos
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )

        return resultado

    def listar_libros_categoria(self, categoria):

        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')
    
    def add_autor_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro


class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()