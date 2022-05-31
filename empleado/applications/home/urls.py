from django.contrib import admin
from django.urls import path



from .  import views
urlpatterns = [
    path("prueba/",views.Pruebaview.as_view()),
    path("lista/",views.PruebaListView.as_view()),
    path("listaprueba/",views.ListapruebaListView.as_view()),
    
    #Url que trabaja con Model form
    path("listacreate/",views.PruebaCreateView.as_view(),name="crear"),
   
]