from django.contrib import admin
from django.urls import path



from .  import views
app_name="departamento_app"
urlpatterns = [
    path(
        "new_departamento/",
        views.NewDepartamentoView.as_view(),
        name="add_departamento"
        ),
    
    path(
        'dep_list/',
         views.DepartamentoListView.as_view(),
          name='lista_departamento'
          ),
   
]