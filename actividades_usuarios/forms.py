from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from actividades_usuarios.models import Avatar


class UserRegisterForm(UserCreationForm):
    # Esto es un ModelForm
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
       model = User
       fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):

   class Meta:
       model = User
       fields = ['first_name', 'last_name', 'email']

# Agregar al final del archivo
class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']