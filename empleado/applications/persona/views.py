#---------------------------------------LIBRERIAS---------------------------------------------
#BASE DE DATOS EMPLEADO
import django
from .models import Empleado
# Create your views here.
#IMPORTA VISTAS GENERICAS
from django.views.generic import ListView,DetailView,CreateView,TemplateView,UpdateView,DeleteView
#Importa redireccionamiento de urls
from django.urls import reverse_lazy
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

#---------------------------------------VISTA 5------------------------------------------------
#Listview  con relacion de muchos a muchos
class Listamanytomany(ListView):
    template_name="persona/manytomany.html"
    context_object_name="habilidades"

    def get_queryset(self):

        lista=Empleado.objects.get(id=1)
        #Objeto que almacena el empleado y sus habilidades correspondientes
        empleado_habilidades=lista.habilidades.all()
        return empleado_habilidades
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 6------------------------------------------------
 #DETAIL VIEW

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/empleadodetail.html"

    def get_context_data(self, **kwargs) :
        context=super(EmpleadoDetailView,self).get_context_data(**kwargs)
        context["titulo"]="Empleado del mes"
        return context
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 7------------------------------------------------

class SuccessView(TemplateView):
    template_name = "persona/success.html"


#CREATE VIEW (POST)
#Recuerda que el objeto con el que se pintara la informacion en el htlm es "form"
class EmpleadoCreateView(CreateView):
    #Modelo
    model = Empleado
    #Template
    template_name = "persona/crearempleado.html"
    #Campos
    fields=["first_name","last_name","job","departamento","departamento","image","habilidades","hoja_vida"]
    #fields=("__all__")
#------------------------------------------------------------------------------------------
 #REDIRECCIONAMIENTO NO RECOMENDADO   
    #Pagina que rediccionara cuando la vista cumpla su cometido "."= el mismo template
    #Url no template
    #success_url= "/success"
#------------------------------------------------------------------------------------------    
#REDIRECCIONAMIENTO CON DJANGO 
# libreria reverse_lazy
#   persona_app (etiqueta de las urls) correcto (name de la url)   
    success_url=reverse_lazy("persona_app:correcto")

    def form_valid(self, form):
        '''
        Cuando lo recibido en el formulario es correcto
        '''
        #Almacena la informacion en la base (Intercepta la informacion guardada)
        empleado=form.save(commit=False)
        print(empleado)
        #Actualiza uno de los campos con la informacion registrada
        empleado.full_name=empleado.first_name +" "+empleado.last_name
        #Actualiza la informacion en la base
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 7------------------------------------------------
#UPDATE VIEW
class EmpleadoUpdateView(UpdateView):
    #Similar al CREATE VIEW
    model = Empleado
    template_name = "persona/empleadoupdate.html"
    fields=["first_name","last_name","job","departamento","departamento","image","habilidades","hoja_vida"]
    success_url=reverse_lazy("persona_app:correcto")

    '''
    def post(self, request, *args, **kwargs):
        
        Esta funcion se ejecuta primero
        Permite obtener los datos desde el la url con request
        
        print("+++++++++++++METODO POST+++++++++++++++++")
        print(request.POST)
        print(request.POST["full_name"])
        print("*****************************************")
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
        '''

    def form_valid(self, form):
        print("+++++++++++++METODO FORM VALID+++++++++++++++++")
        '''
        Cuando lo recibido en el formulario es correcto
        '''
        #Almacena la informacion en la base (Intercepta la informacion guardada)
        empleado=form.save(commit=False)
        print(empleado)
        #Actualiza uno de los campos con la informacion registrada
        empleado.full_name=empleado.first_name +" "+empleado.last_name
        #Actualiza la informacion en la base
        empleado.save()
        return super(EmpleadoUpdateView,self).form_valid(form)
#----------------------------------------------------------------------------------------------

#---------------------------------------VISTA 8------------------------------------------------
#DELETE VIEW

class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/deletepersona.html"
    success_url=reverse_lazy("persona_app:correcto")