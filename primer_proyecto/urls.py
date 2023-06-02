"""
URL configuration for primer_proyecto project.

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
from django.conf import settings
from django.conf.urls.static import static

from primer_proyecto.views import saludar, saludar_con_fecha, saludar_con_html, saludar_a_usuario, inicio

from club_once_estrellas.models import Socios, Actividades, Salones


urlpatterns = [
    path("", inicio, name="inicio"),
    path('admin/', admin.site.urls),
    path('', include('club_once_estrellas.urls')),
    path('', include('actividades_usuarios.urls')),
    path("Saludo/", saludar),
    path("saludo-hoy/", saludar_con_fecha),
    path("saludar-html/", saludar_con_html),
    path("Hola/<nombre>/", saludar_a_usuario),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)