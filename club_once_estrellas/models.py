from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Socios(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    apellido = models.CharField(max_length=64)
    cedula_de_identidad = models.CharField(max_length=8)
    direccion = models.CharField(max_length=64)
    celular = models.CharField(max_length=20)
    numero_socio = models.CharField(max_length=128)
    es_socio = models.BooleanField(default=False) # Booleano que me dice si es o no socio. 
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
class Actividades(models.Model):
    actividad = models.CharField(max_length=64)
    horario = models.TimeField()
    dia = models.CharField(max_length=64)
    nombre_profesor = models.CharField(max_length=64)
    telefono_contacto = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='Actividades', null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Actividades', null=True, blank=True)
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"{self.actividad}, {self.telefono_contacto}"
    
class Articulos(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='articulos', null=True, blank=True)
    fecha_publicacion = models.DateField()
    imagen = models.ImageField(upload_to='articulos/')
    comentarios = models.ManyToManyField('Comentario', blank=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    

class Salones(models.Model):
    tipo = models.CharField(max_length=64)
    horario = models.TimeField()
    precio = models.IntegerField()
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class InformacionSocios(models.Model):
    beneficios = models.TextField()
    cuota_social = models.DecimalField(max_digits=8, decimal_places=2)
    formas_pago = models.CharField(max_length=100)
