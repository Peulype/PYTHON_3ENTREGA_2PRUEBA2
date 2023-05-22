"""
URL configuration for sistema_coder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from club_once_estrellas.views import exito


from club_once_estrellas.views import lista_de_actividades, Salones_en_alquiler, lista_de_socios, agregar_salon, buscar_salon, exito, \
    eliminar_salon
  


urlpatterns = [
    path("actividades/", lista_de_actividades, name="lista_actividades"),
    path("salones/", Salones_en_alquiler, name="lista_salones"),
    path("Sociosonce/", lista_de_socios, name= "lista_de_socios"),
    path("agregar-salon/", agregar_salon, name= "agregar_salon"),
    path("borrar-salon/<int:id>/", eliminar_salon, name= "eliminar_salon"),
    path("buscar-salon/", buscar_salon, name= "buscar_salon"),
    path("exito/", exito, name="exito")
    ]

