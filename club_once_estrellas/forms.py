from django import forms


class SalonesFormulario(forms.Form):
    tipo = forms.CharField(required=True, max_length=64) 
    horario = forms.TimeField(required=True)
    precio = forms.IntegerField(required=True, max_value=50000)