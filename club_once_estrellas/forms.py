from django import forms
from .models import Actividades


class SalonesFormulario(forms.Form):
    tipo = forms.CharField(required=True, max_length=64) 
    horario = forms.TimeField(required=True)
    precio = forms.IntegerField(required=True)

class ActividadesForm(forms.ModelForm):
    class Meta:
        model = Actividades
        fields = ('actividad', 'horario', 'dia', 'nombre_profesor', 'telefono_contacto')