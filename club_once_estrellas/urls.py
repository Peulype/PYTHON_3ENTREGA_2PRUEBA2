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

from club_once_estrellas.views import lista_de_actividades, Salones_en_alquiler, Socios_socias


urlpatterns = [
    path("actividades/", lista_de_actividades, name="lista_para_actividades"),
    path("salones/", Salones_en_alquiler, name="lista_salones"),
    path("Socios_once/", Socios_socias, name= "Socios_as")

]