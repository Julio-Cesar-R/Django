#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS EMPLEADO
from .models import Empleado
# Create your views here.
#IMPORTA VISTAS GENERICAS
from django.views.generic import ListView
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 1------------------------------------------------
#Vista que enlista todos los empleados de la tabla empleados
class Listallempleados(ListView):
    #Template donde se pintara la informacion
    template_name= "persona/listall.html"
    #Paginacion 
    #Agregar en la url /?page=1 y mostrara la informacion de esa pagina
    paginate_by=1
    #Ordenar
    ordering="first_name"
    #informacion de la base empleado que se mostrara
    model=Empleado
    #Variable que se debe pintar en el archivo html
    #context_object_name= "lista_empleados"
#----------------------------------------------------------------------------------------------
    


#---------------------------------------VISTA 2------------------------------------------------
#Vista que enlista todos los empleados por area determinada
class Listarea(ListView):
    #Template donde se pintara la informacion
    template_name= "persona/listarea.html"
    
    #Funcion que recibe informacion mediante la URL
    def get_queryset(self):
        #Variable que almacena el valor ingresador en la URL
        #Recibe un parametro mediante una url
        area=self.kwargs["area"]
        #Compara la informacion recibida en la url con la de la base
        lista=Empleado.objects.filter(departamento__name=area)
        return lista
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 3------------------------------------------------
#Vista que filtra al empleado mediante el "trabajo" 
#Recordar que lo que se ingresara en la url sera el numero correspondiente al empleado
class Listatrabajo(ListView):
    #Template donde se pintara la informacion
    template_name= "persona/listatrabajo.html"
    
    def get_queryset(self):
        #Variable que almacena el valor ingresador en la URL
        #Recibe un parametro mediante una url
        trabajo=self.kwargs["trabajo"]
        #Compara la informacion recibida en la url con la de la base
        lista=Empleado.objects.filter(job=trabajo)
        return lista
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 4------------------------------------------------
#Genera una busqueda en la tabla empleados mediante una caja de texto
class Listaempleadokey(ListView):
    #Template donde se pintara la informacion
    template_name="persona/listaempleadokey.html"
    #Objeto que envia la informacion al html
    context_object_name= "empleados"

    #Funcion que recibe la informacion desde una caja de texto desde el html
    def get_queryset(self):
        print("*******")
        #Obtiene la informacion del formulario con metodo Get
        palabra_clave=self.request.GET.get("kword", "")
        print("*********",palabra_clave)
        #Compara la informacion recibida en el input con la de la base
        lista=Empleado.objects.filter(first_name=palabra_clave)
        return lista
#----------------------------------------------------------------------------------------------