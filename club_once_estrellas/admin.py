from django.contrib import admin

# Register your models here.
from django.contrib import admin

from club_once_estrellas.models import Socios, Actividades, Salones


admin.site.register(Socios)
admin.site.register(Actividades)
admin.site.register(Salones)
