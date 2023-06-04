from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Avatar(models.Model):
     #Avatar es una tabla anexa de User
     #Relacion con la tabla User
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    # upload_to es la subcarpeta dentro de la carpeta media
    imagen = models.ImageField(upload_to='avatares', default='avatares/generica.jpg', null=True, blank=True)

    def __str__(self):
        return f"Avatar de: {self.user}"
