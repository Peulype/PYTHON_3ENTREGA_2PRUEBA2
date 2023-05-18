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
    http_responde = render(
        request=request,
        template_name='club_once_estrellas/lista_actividades.html',
        context=contexto,
    )
    return http_responde