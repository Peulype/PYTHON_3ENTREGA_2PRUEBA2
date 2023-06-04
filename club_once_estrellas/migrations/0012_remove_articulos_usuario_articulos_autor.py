# Generated by Django 4.2 on 2023-06-02 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club_once_estrellas', '0011_rename_autor_articulos_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='usuario',
        ),
        migrations.AddField(
            model_name='articulos',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='articulos', to=settings.AUTH_USER_MODEL),
        ),
    ]