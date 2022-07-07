#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path


#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------

app_name="app1_app"

urlpatterns = [
    #Urls Template view (pagina comun) 
    path('demostracion/', views.DemostracionCreateView.as_view(), name='create_demostracion'),
    #Urls APIs
    path('api_view_demostracion/',views.DemostracionAPIView.as_view(), name='listar_demostracion'),
    path('api_create_demostracion/',views.DemostracionAPICreatee.as_view(), name='crear_demostracion'),

]