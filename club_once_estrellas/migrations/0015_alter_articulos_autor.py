# Generated by Django 4.2 on 2023-06-02 11:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('club_once_estrellas', '0014_alter_articulos_autor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulos',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]