from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def lista_de_actividades(request):
    contexto = {
        "Actividades": [
            {"actividad": "Tambores", "telefono_contacto": "099123456"},
            {"actividad": "Taekwoondo", "telefono_contacto": "098123456"},
            {"actividad": "Folklore", "telefono_contacto": "097123456"},
            {"actividad": "Danza", "telefono_contacto": "096123456"},
        ]
    }
    http_response = render(
        request=request,
        template_name='club_once_estrellas/lista_actividades.html',
        context=contexto,
    )
    return http_response

def Salones_en_alquiler(request):
    contexto = {
        "Salones": [
            {"tipo": "Social", "precio": "5000"},
            {"tipo": "Parrilla chica", "precio": "3100"},
            {"tipo": "Parrilla grande", "precio": "4800"},
            {"tipo": "Carabelas", "precio": "4500"},
        ]
    }
    http_response = render(
        request=request,
        template_name='club_once_estrellas/lista_salones.html',
        context=contexto,
    )
    return http_response

def lista_de_socios(request):
    contexto = {
        "Socios": [
            {"nombre": "Pau", "apellido": "P"},
            {"nombre": "Anita", "apellido": "R"},
            {"nombre": "Juan", "apellido": "M"},
        ]
    }
    http_response = render(
        request=request,
        template_name='club_once_estrellas/lista_socios.html',
        context=contexto,
    )
    return http_response

