from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from club_once_estrellas.models import Articulos
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from .forms import ActividadesForm

from club_once_estrellas.models import Actividades, Salones
from club_once_estrellas.forms import SalonesFormulario
from club_once_estrellas.models import InformacionSocios

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy



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

def index(request):
    actividades = Actividades.objects.all()
    context = {'actividades': actividades}
    return render(request, 'club_once_estrellas/lista_actividades.html', context)

# Vista de lista de actividades
class ActividadesListView(ListView):
    model = Actividades
    template_name = 'club_once_estrellas/lista_actividades.html'
    context_object_name = 'actividades'

# Vista de creación de actividades
class ActividadesCreateView(LoginRequiredMixin, CreateView):
    model = Actividades
    fields = ('actividad', 'horario', 'dia', 'nombre_profesor', 'telefono_contacto')
    template_name = 'club_once_estrellas/actividades_form.html'
    success_url = reverse_lazy('lista_actividades')
    success_message = "Actividad creada con éxito"

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
# Vista de detalle de actividades
class ActividadesDetailView(DetailView):
    model = Actividades
    template_name = 'club_once_estrellas/actividades_detail.html'
    context_object_name = 'actividad'

# Vista de actividades formato articulo
#def actividad_article(request, pk):
 #   actividad = get_object_or_404(Actividades, pk=pk)
  #  return render(request, 'club_once_estrellas/actividad_article.html', {'actividad': actividad})

class ArticulosListView(ListView):
    model = Articulos
    template_name = 'club_once_estrellas/lista_articulos.html'
    context_object_name = 'articulos'

class ArticuloDetailView(DetailView):
    model = Articulos
    template_name = 'club_once_estrellas/detalle_articulo.html'
    context_object_name = 'articulo'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
    
@method_decorator(login_required, name='dispatch')
class ArticuloCreateView(CreateView):
    model = Articulos
    fields = ['titulo', 'subtitulo', 'descripcion', 'autor', 'fecha_publicacion', 'imagen']
    template_name = 'club_once_estrellas/crear_articulo.html'
    success_url = reverse_lazy('lista_articulos')

    def form_valid(self, form):
        # Guardar el artículo
        self.object = form.save()

        # Establecer el mensaje de éxito
        messages.success(self.request, 'Artículo creado exitosamente.')

        return super().form_valid(form)

class ArticuloDeleteView(UserPassesTestMixin, DeleteView):
    model = Articulos
    template_name = 'club_once_estrellas/articulo_confirm_delete.html'
    success_url = reverse_lazy('lista_articulos')

    @method_decorator(login_required)  # Requiere inicio de sesión
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        articulo = self.get_object()
        return self.request.user.username == articulo.autor

# Vista de actualización de actividades

@login_required
def ActividadesUpdateView(request, pk):
    actividad = get_object_or_404(Actividades, pk=pk)

    if request.user != actividad.usuario:
        messages.error(request, "No tienes permiso para editar esta actividad.")
        return redirect('lista_actividades')

    if request.method == 'POST':
        form = ActividadesForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            messages.success(request, "Actividad editada con éxito.")
            return redirect('lista_actividades')
    else:
        form = ActividadesForm(instance=actividad)

    return render(request, 'club_once_estrellas/actividades_edit_form.html', {'form': form})

# Vista de eliminación de actividades

@login_required
def ActividadesDeleteView(request, pk):
    actividad = get_object_or_404(Actividades, pk=pk)

    # Comprobar si el usuario actual es el usuario de la actividad
    if actividad.usuario == request.user:
        if request.method == 'POST':
            actividad.delete()
            return redirect('lista_actividades')
        else:
            context = {'actividad': actividad}
            return render(request, 'club_once_estrellas/actividades_confirm_delete.html', context)
    else:
        error_message = "No tienes permiso para eliminar esta actividad."
        context = {'error_message': error_message}
        return render(request, 'club_once_estrellas/actividades_confirm_delete.html', context)



def about(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='club_once_estrellas/about.html',
        context=contexto,
    )
    return http_response
