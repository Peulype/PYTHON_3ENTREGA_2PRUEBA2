from django.db import models

# Create your models here.
class Socios(models.Model):
    nombre = models.CharField(max_length=64)  # Equivalente de str
    apellido = models.CharField(max_length=64)
    cedula_de_identidad = models.CharField(max_length=8)
    direccion = models.CharField(max_length=64)
    celular = models.CharField(max_length=20)
    numero_socio = models.CharField(max_length=128)
    es_socio = models.BooleanField(default=False) # Booleano que me dice si es o no socio. 

class Actividades(models.Model):
    actividad = models.CharField(max_length=64)
    horario = models.TimeField()
    dia = models.IntegerField()
    nombre_profesor = models.CharField(max_length=64)
    telefono_contacto = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.actividad}, {self.telefono_contacto}"
    
class Actividad(models.Model):
    foto = models.ImageField(upload_to='actividades/')
    descripcion = models.TextField()
    nombre_profesor = models.CharField(max_length=100)
    telefono_contacto = models.CharField(max_length=20)

class Salones(models.Model):
    tipo = models.CharField(max_length=64)
    horario = models.TimeField()
    precio = models.IntegerField()

class InformacionSocios(models.Model):
    beneficios = models.TextField()
    cuota_social = models.DecimalField(max_digits=8, decimal_places=2)
    formas_pago = models.CharField(max_length=100)
