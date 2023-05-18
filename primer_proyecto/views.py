from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def saludar(request):
    saludo = "Bienvenido al Once"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo = f"Hola querido usuario, fecha: {hoy.day}/{hoy.month}"
    pagina_html = HttpResponse(saludo)
    return pagina_html

def saludar_con_html(request):
    contexto = {}
    http_responde = render(
        request = request,
        template_name='club_once_estrellas/base.html',
        context=contexto,
    )
    return http_responde

def saludar_a_usuario(request, nombre):
    texto = f"Hola {nombre}"
    http_response = HttpResponse(texto)
    return http_response