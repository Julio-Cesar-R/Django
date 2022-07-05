from django.shortcuts import render

from django.views.generic import ListView, DetailView

# mdols local
from .models import Libro,Categoria


class ListLibros(ListView):
    '''
    Esta vista se encarga de mostrar los libros por una fecha determinada
    por el programador y por el usuario
    '''
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        '''
        1- Muestra los libros en el cual la fecha de lanzamiento este en 
        el rango de F1 y F2
        
        2-Muestra los libros que coincidan con  la "kword" ingresada por el usuario y 
        una fecha determinada por el sistema
        '''
        palabra_clave = self.request.GET.get("kword", '')
        #fecha 1
        f1 = self.request.GET.get("fecha1", '')
        #fecah 2
        f2 = self.request.GET.get("fecha2", '')

        
        if f1 and f2:
            return Libro.objects.listar_libros2(palabra_clave, f1, f2)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrg(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Libro.objects.listar_libros_trg(palabra_clave)


class ListLibros2(ListView):
    '''
    Esta vista muestra la informacion de libros 
    filtrados por categoria
    '''
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')
        return Libro.objects.listar_libros_categoria(palabra_clave)





class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"

