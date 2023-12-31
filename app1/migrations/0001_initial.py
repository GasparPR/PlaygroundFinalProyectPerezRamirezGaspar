# Generated by Django 4.2.4 on 2023-09-19 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='default', max_length=200)),
                ('usuario', models.CharField(default='default', max_length=200)),
                ('tecnologia', models.CharField(default='default', max_length=15)),
                ('marca', models.CharField(default='default', max_length=40)),
                ('modelo', models.CharField(default='default', max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('telefonoContacto', models.IntegerField()),
                ('emailContacto', models.EmailField(default='example@example.com', max_length=254)),
                ('imagenTecnologia', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
            options={
                'ordering': ['usuario', '-fechaPublicacion'],
            },
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('fechaComentario', models.DateTimeField(auto_now_add=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='app1.tecnologia')),
            ],
            options={
                'ordering': ['-fechaComentario'],
            },
        ),
    ]
