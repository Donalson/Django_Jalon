# Generated by Django 4.0.6 on 2022-08-05 19:00

import Usuarios.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0005_alter_usuario_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Docidentificacion',
            field=models.CharField(default=-12345, max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Selfie1',
            field=models.ImageField(blank=True, null=True, upload_to=Usuarios.models.ruta_personalizada_S1),
        ),
    ]