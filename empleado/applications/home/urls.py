from django.contrib import admin
from django.urls import path



from .  import views
urlpatterns = [
    path("prueba/",views.Pruebaview.as_view()),
    path("lista/",views.PruebaListView.as_view()),
    path("listaprueba/",views.ListapruebaListView.as_view()),
    path('resumen_foundation/', views.Resumenfoundationview.as_view(), name='res_foundation'),
    #Url que trabaja con Model form
    path("listacreate/",views.PruebaCreateView.as_view(),name="crear"),
   
]