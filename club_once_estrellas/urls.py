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

from club_once_estrellas.views import (index, Salones_en_alquiler, lista_de_socios, agregar_salon, buscar_salon, exito, \
    eliminar_salon, editar_salones, ArticuloDeleteView, ArticulosListView, ActividadesListView, ActividadesCreateView, \
    ActividadesDetailView, ActividadesUpdateView, ActividadesDeleteView, ArticuloCreateView, ArticuloDetailView, about)




urlpatterns = [
    path("salones/", Salones_en_alquiler, name="lista_salones"),
    path("Sociosonce/", lista_de_socios, name="lista_de_socios"),
    path("agregar-salon/", agregar_salon, name="agregar_salon"),
    path("editar-salon/<int:id>/", editar_salones, name="editar_salon"),
    path("borrar-salon/<int:id>/", eliminar_salon, name="eliminar_salon"),
    path("buscar-salon/", buscar_salon, name="buscar_salon"),
    path("exito/", exito, name="exito"),
    path('', index, name='index'),
    path("actividades/", ActividadesListView.as_view(), name="lista_actividades"),
    path("actividades/<int:pk>/", ActividadesDetailView.as_view(), name="ver_actividad"),
    path('crear-articulo/', ArticuloCreateView.as_view(), name='crear_articulo'),
    path('eliminar-articulo/<int:pk>/', ArticuloDeleteView.as_view(), name='eliminar_articulo'),
    path('articulos/', ArticulosListView.as_view(), name='lista_articulos'),
    path('articulos/<int:pk>/', ArticuloDetailView.as_view(), name='detalle_articulo'),
    path("actividades/crear/", ActividadesCreateView.as_view(), name="crear_actividad"),
    path("actividades/editar/<int:pk>/", ActividadesUpdateView, name="editar_actividad"),
    path("actividades/eliminar/<int:pk>/", ActividadesDeleteView, name="eliminar_actividad"),
    path("about/", about, name="about"),
]

