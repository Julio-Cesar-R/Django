from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(
        'prestamos/',
        views.PrestamoListView.as_view(),
        name='prestamo_all'
    ),

    path(
        'prestamo/add/', 
        views.AddPrestamo.as_view(), 
        name="prestamo_add"
    ),
    path(
        'prestamo/multiple-add/', 
        views.AddMultiplePrestamo.as_view(), 
        name="prestamo_add_multiple"
    ),
]