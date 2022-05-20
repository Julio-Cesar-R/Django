from django.contrib import admin
from django.urls import path



from .  import views
urlpatterns = [
    path("departamento/",views.Departamentoview.as_view()),
   
]