# Generated by Django 4.2.4 on 2023-09-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tecnologia',
            old_name='imagentecnologia',
            new_name='imagenTecnologia',
        ),
        migrations.AlterField(
            model_name='tecnologia',
            name='tecnologia',
            field=models.CharField(default='cpu', max_length=15),
        ),
    ]
