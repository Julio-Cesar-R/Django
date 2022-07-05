import datetime

from django.db import models

from django.db.models import Q, Count
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
        Manejador que filtra libros por una
        palabra clave y dos fechas dadas

        Funcion que recibe 3 parametros
        kword : Titulo del libro
        fecha1: Rango de fecha inicial
        fecha2: Rango de fecha limite

        return: -Coincidencia de nombres
                -Coincidencia entre rango de fechas
        '''
        #Se le da un formato de fecha a los parametros recibidos en el formulario
        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d").date()
        
        #Consulta a la base de datos
        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )

        return resultado

    def listar_libros_categoria(self, kword):
        '''
        Manejador que filtra libros por categoria
        '''
        resultado= self.filter(
            categoria__id__contains=kword
        ).order_by('titulo')
        if resultado:
            return resultado
            
        else:
            resultado= self.filter(
                categoria__nombre__icontains=kword
            ).order_by("titulo")
            return resultado
    
    def add_autor_libro(self, libro_id, autor):
        '''
        Agrega un autor al libro seleccionado mediante ids
        '''
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro
    
    def libro_num(self):
        '''
        Funcion que regresa el numero de prestamos
        con Aggregate (devuelve un diccionario)
        a diferencia de annotate que se utiliza usando una consulta y devuelve un queryset

        '''
        resultado=self.aggregate(
            numero_prestamos=Count("Prestamo_libro")

        )
        return resultado


class CategoriaManager(models.Manager):
    """ managers para el modelo autor """

    def categoria_por_autor(self, autor):
        print("*******************")
        print(autor)
        '''
        Consulta con foreing_key
        Retorna la informacion del autor en base a una categoria
        "Es importante el related_name dentro del modelo libro para especificar la union de dos tablas"
        campo del modelo Libro en el atributo categoria related_name="categoria_libro"
        '''
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categoria_libro(self):
        '''
        Devuelve el numero de libros por categoria
        Count
        Annotate
        '''
        resultado=self.annotate(
            num_libros=Count("categoria_libro")
        )
        
        for r in resultado:
            print("************")
            print(r,r.num_libros)
        return resultado
#_---------------------------------------------------------------------------------------
#Probar consultas sin necesidad de crear las vistas (Shell )
#Python manage.py shell
#>>>from applications.libro.models import *
#>>>Categoria.objects.categoria_por_autor("1")
#-----------------------------------------------------------------------------------------
