from django.contrib import admin
from django.urls import path



from .  import views
urlpatterns = [
    path(
        "new_departamento/",
        views.NewDepartamentoView.as_view(),
        name="add_departamento"
        ),
   
]