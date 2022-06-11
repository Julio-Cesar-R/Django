#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path
#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------



#--------------------------------------------URLS----------------------------------------------
#Etiqueta con la que se identifica el conjunto de urls
app_name="persona_app"

urlpatterns = [
    #Urls Template view (pagina comun) 
    path(
        "success/",
        views.SuccessView.as_view(),
        #nombre con el que se identificara la ruta
        name="correcto"
        ),
    #Urls y el nombre las vistas
    path('admin_empleado/',views.Lista_admin.as_view(), name='administrador'),

    path("lista_todo_empleado/",views.Listallempleados.as_view(),name="empleados_all"),
    path('api_lista_todo_empleado/', views.EmpleadolistAPIview.as_view(), name='api_all_empleados'),




    path("lista_by_key/",views.Listaempleadokey.as_view()),
    path("many_to_many/",views.Listamanytomany.as_view()),   
    #Url/variable que recibe la informacion en la url
    path("lista_by_area/<area>",views.Listarea.as_view(),name="area_empleados"),
    path("lista_by_job/<trabajo>",views.Listatrabajo.as_view()),
    
    #Url de una vista de detalle (detail view)
    path("detail_view_empleado/<pk>",views.EmpleadoDetailView.as_view(),name="detail_empleado"),
    
    
    #Url de una vista Create
    path(
        "create_empleado/",
        views.EmpleadoCreateView.as_view(),
        name="create_empleado"
        ),
    
    #Url de una vista updatevier
    path(
        "update_empleado/<pk>/",
        views.EmpleadoUpdateView.as_view(),
        name="update_empleado"
        ),
    #Url de una vista delete view
    path(
        "delete_empleado/<pk>/",
        views.EmpleadoDeleteView.as_view(),
        name="delete_empleado"
        ),
    #Url que carga la pagina principal
    path(
        '',
        views.InicioView.as_view(),
        name='home'
    ),

]
#----------------------------------------------------------------------------------------------