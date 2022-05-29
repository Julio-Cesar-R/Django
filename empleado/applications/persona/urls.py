#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path
#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------



#--------------------------------------------URLS----------------------------------------------
urlpatterns = [
    #Urls y el nombre las vistas
    path("lista_todo_empleado/",views.Listallempleados.as_view()),
    path("lista_by_key/",views.Listaempleadokey.as_view()),  
    #Url/variable que recibe la informacion en la url
    path("lista_by_area/<area>",views.Listarea.as_view()),
    path("lista_by_job/<trabajo>",views.Listatrabajo.as_view()),
     
]
#----------------------------------------------------------------------------------------------