from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from club_once_estrellas.models import Salones
from club_once_estrellas.forms import SalonesFormulario
from club_once_estrellas.models import InformacionSocios, Actividad, Actividades

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#no usado - cambiamos por vistas basadas en clases
# def lista_de_actividades(request):
#     contexto = {
#         "Actividades": [
#             {"actividad": "Tambores", "telefono_contacto": "099123456"},
#             {"actividad": "Taekwoondo", "telefono_contacto": "098123456"},
#             {"actividad": "Folklore", "telefono_contacto": "097123456"},
#             {"actividad": "Danza", "telefono_contacto": "096123456"},
#         ]
#     }
#     http_response = render(
#         request=request,
#         template_name='club_once_estrellas/lista_actividades.html',
#         context=contexto,
#     )
#     return http_response

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
    informacion_socios = InformacionSocios.objects.first()  # Recupera el primer objeto de InformacionSocios o ajusta la consulta según tus necesidades

    contexto = {
        "informacion_socios": informacion_socios,
    }

    http_response = render(
        request=request,
        template_name='club_once_estrellas/lista_socios.html',
        context=contexto,
    )
    
    return http_response

@login_required
def agregar_salon_version1(request):
    #No se usa 
    if request.method == "POST":
        data = request.POST
        tipo = data["tipo"]
        horario = data["horario"]
        precio = data["precio"]
        salones = Salones(tipo=tipo, horario=horario, precio=precio)
        salones.save()
        Url_exitosa = reverse("lista_salones")
        return redirect(Url_exitosa)
    else:
        http_response = render(
            request=request,
            template_name='club_once_estrellas/formulario_a_mano.html',
            

    )
    return http_response

@login_required
def agregar_salon(request):
    if request.method == "POST":
        formulario = SalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            tipo = data["tipo"]
            horario = data["horario"]
            precio = data["precio"]
            creador = request.user
            salon = Salones(tipo=tipo, horario=horario, precio=precio, creador=creador)
            salon.save()
            #return redirect("exito")  # Redirige a la página de éxito

            # Redirecciono al usuario a la lista de salones
            url_exitosa = reverse('lista_salones')  # estudios/salones/
            return redirect(url_exitosa)
    else:  # GET
        formulario = SalonesFormulario()
    http_response = render(
        request=request,
        template_name='club_once_estrellas/formulario_salones.html',
        context={'formulario': formulario}
        )
    return http_response

def exito(request):
    return render(request, 'club_once_estrellas/exito.html')

def buscar_salon(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        salones = Salones.objects.filter(tipo__contains=busqueda)
        contexto = {
            'Salones': salones,
            }

        http_response = render(
            request=request,
            template_name='club_once_estrellas/lista_salones.html',
            context=contexto,
        )
        return http_response
@login_required    
def eliminar_salon(request, id):
    salones = Salones.objects.get(id=id)
    if request.method == "POST":
        salones.delete()
        url_exitosa = reverse('lista_salones')
        return redirect(url_exitosa)

@login_required
def editar_salones(request, id):
    salon = Salones.objects.get(id=id)

    if request.method == "POST":
        formulario = SalonesFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            salon.tipo = data["tipo"]
            salon.horario = data["horario"]
            salon.precio = data["precio"]
            salon.creador = request.user



            # Actualizar los campos del salón existente en lugar de crear uno nuevo
            #salon.tipo = tipo
            #salon.horario = horario
            #salon.precio = precio
            #salon.save()

            url_exitosa = reverse('lista_salones')
            return redirect(url_exitosa)
    else:  # GET
        # Usar los valores actuales del salón para prellenar el formulario
        inicial = {
            'tipo': salon.tipo,
            'horario': salon.horario,
            'precio': salon.precio,
        }
        formulario = SalonesFormulario(initial=inicial)

    return render(
        request=request,
        template_name='club_once_estrellas/formulario_salones.html',
        context={'formulario': formulario, 'salon': salon,},
    )


def lista_de_actividades1(request):
    if request.method == 'POST':
        nueva_actividad = Actividad()
        nueva_actividad.foto = request.FILES['foto']
        nueva_actividad.descripcion = request.POST['descripcion']
        nueva_actividad.nombre_profesor = request.POST['nombre_profesor']
        nueva_actividad.telefono_contacto = request.POST['telefono_contacto']
        nueva_actividad.save()
        
        # Realizar cualquier otra acción después de guardar la actividad
        
        return HttpResponse('Actividad creada exitosamente')

    return render(request, 'lista_actividades.html')

# Vistas de Actividades
class ActividadesListView(ListView):
    model = Actividades
    template_name = 'club_once_estrellas/lista_actividades.html'


class ActividadesCreateView(LoginRequiredMixin, CreateView):
    model = Actividades
    fields = ('actividad', 'horario', 'dia', 'nombre_profesor', 'telefono_contacto')
    success_url = reverse_lazy('lista_actividades')


class ActividadesDetailView(DetailView):
    model = Actividades
    success_url = reverse_lazy('lista_actividades')


class ActividadesUpdateView(LoginRequiredMixin, UpdateView):
    model = Actividades
    fields = ('actividad', 'horario', 'dia', 'nombre_profesor', 'telefono_contacto')
    success_url = reverse_lazy('lista_actividades')


class ActividadesDeleteView(LoginRequiredMixin, DeleteView):
    model = Actividades
    success_url = reverse_lazy('lista_actividades')