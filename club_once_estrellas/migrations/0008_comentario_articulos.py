# Generated by Django 4.2 on 2023-06-02 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club_once_estrellas', '0007_alter_actividades_imagen_alter_actividades_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('contenido', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('autor', models.CharField(max_length=100)),
                ('fecha_publicacion', models.DateField()),
                ('imagen', models.ImageField(upload_to='articulos/')),
                ('comentarios', models.ManyToManyField(blank=True, to='club_once_estrellas.comentario')),
            ],
        ),
    ]