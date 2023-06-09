# Generated by Django 4.2 on 2023-05-31 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club_once_estrellas', '0006_remove_actividades_creador_actividades_comentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actividades',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='Actividades'),
        ),
        migrations.AlterField(
            model_name='actividades',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Actividades', to=settings.AUTH_USER_MODEL),
        ),
    ]
