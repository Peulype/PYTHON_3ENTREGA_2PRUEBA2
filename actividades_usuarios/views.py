from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from actividades_usuarios.forms import UserRegisterForm, UserUpdateForm, AvatarFormulario
from actividades_usuarios.models import Avatar


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()  # Esto lo puedo usar porque es un model form
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:  # GET
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='actividades_usuarios/registro.html',
        context={'form': formulario},
    )

def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('inicio')
                return redirect(url_exitosa)
    else:  # GET
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='actividades_usuarios/login.html',
        context={'form': form},
    )


class CustomLogoutView(LogoutView):
   template_name = 'actividades_usuarios/logout.html'


class MiPerfilUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'actividades_usuarios/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


def agregar_avatar(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = formulario.save(commit=False)
            avatar.user = request.user

            # Guarda la imagen en el sistema de archivos
            if avatar.imagen:
                fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                filename = fs.save(avatar.imagen.name, avatar.imagen)
                avatar.imagen = filename

            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario()

    return render(
        request=request,
        template_name="actividades_usuarios/formulario_avatar.html",
        context={'form': formulario},
    )
