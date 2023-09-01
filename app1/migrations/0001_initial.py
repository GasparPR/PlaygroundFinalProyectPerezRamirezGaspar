
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
                ('titulo', models.CharField(max_length=200)),
                ('usuario', models.CharField(max_length=200)),
                ('tecnologia', models.CharField(choices=[('teclado', 'Tecladó'), ('monitor', 'Monitor'), ('mouse', 'Mouse'), ('cpu', 'Cpu'), ('auriculares', 'Auriculares'), ('parlante', 'Parlantes'), ('otro', 'Otro')], default='cpu', max_length=15)),
                ('marca', models.CharField(max_length=40)),
                ('modelo', models.CharField(max_length=40)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('year', models.IntegerField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('telefonoContacto', models.IntegerField()),
                ('emailContacto', models.EmailField(max_length=254)),
                ('imagentecnologia', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
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
