# Generated by Django 4.0.6 on 2022-08-06 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Usuarios', '0007_alter_usuario_verificado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Depositos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Banco', models.CharField(max_length=20)),
                ('NoCuenta', models.CharField(max_length=20)),
                ('Monto', models.FloatField()),
                ('Depositado', models.BooleanField(blank=True, null=True)),
                ('Mensaje', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Usuarios.usuario')),
            ],
        ),
    ]
