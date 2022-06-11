#---------------------------------------LIBRERIAS---------------------------------------------
#Libreria path
from django.urls import path




#Importar el archivo donde se encuentran las vistas
from .  import views
#----------------------------------------------------------------------------------------------

app_name="persona_app"

urlpatterns = [
    #Urls Template view (pagina comun) 
    path('persona_lista/', views.PersonaListView.as_view(), name='persona_lista'),
    path('api_persona_lista/', views.PersonlistAPIview.as_view(), name='api_lista_personas'),


    path("lista_by_pk/<pk>",views.PersonapkListView.as_view(),name="pk_empleados"),
    path("api_lista_by_pk/<pk>/",views.PersonpkAPIview.as_view(),name="api_pk_empleados"),

    path('add_persona/', views.PersonAddCreateView.as_view(), name='add_persona'),
    path('api_add_persona/', views.PersonAPIcreate.as_view(), name='api_add_persona'),
    
    path('update_persona/<pk>', views.PersonUpdateView.as_view(), name='update_persona'), 
    path('api_update_persona/<pk>', views.PersonAPIUpdate.as_view(), name='api_update_persona'), 
    path('api_retrieve_update_persona/<pk>', views.PersonAPIUpdateretrieve.as_view(), name='api_retrieve_update_persona'), 

    path('delete_persona/<pk>', views.PersonDeleteView.as_view(), name='delete_persona'),  
    path('api_delete_persona/<pk>', views.PersonAPIDelete.as_view(), name='api_delete_persona'),
    path('api_retrieve_delete_persona/<pk>', views.PersonAPIDeleteretrieve .as_view(), name='api_retrieve_delete_persona'), 

 #    
    path('api_personas_serializer/', views.PersonlistAPIserializer .as_view(), name='api_serializer_list_persona'),
    path('api_personas_serializer2/', views.PersonlistAPIserializer2 .as_view(), name='api_serializer_list_persona2'),

    #---------------------------------------------------------------------
    #Serializadores Many to many y foreing key
    path('api_reunion/', views.ReunionApi.as_view(), name='api_reunion'),
    path('api_personas_serializer3/', views.PersonlistAPIserializer3 .as_view(), name='api_serializer_list_persona3'),
]