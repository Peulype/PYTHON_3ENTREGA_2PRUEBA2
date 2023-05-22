from django.shortcuts import render, redirect
from django.urls import reverse

from club_once_estrellas.models import Salones
from club_once_estrellas.forms import SalonesFormulario


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
        "Salones": Salones.objects.all(),
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

def agregar_salon_version1(request):
    if request.method == "POST":
        data = request.POST
        tipo = data["tipo"]
        horario = data["horario"]
        precio = data["precio"]
        salon = Salones(tipo=tipo, horario=horario, precio=precio)
        salon.save()
        Url_exitosa = reverse("lista_salones")
        return redirect(Url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='club_once_estrellas/formulario_a_mano.html',
            

    )
    return http_response

def agregar_salon(request):
    if request.method == "POST":
        formulario = SalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            tipo = data["tipo"]
            horario = data["horario"]
            precio = data["precio"]
            salon = Salones(tipo=tipo, horario=horario, precio=precio)
            salon.save()

            Url_exitosa = reverse("lista_salones")
            return redirect(Url_exitosa)

    else:
        formulario = SalonesFormulario()
    http_response = render(
            request=request,
            template_name='club_once_estrellas/formulario_salones.html',
            context={'formulario': formulario}

    )
    return http_response

