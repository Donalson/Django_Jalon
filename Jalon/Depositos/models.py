from django.db import models
from Usuarios.models import Usuario

# Create your models here.

class Depositos(models.Model):
    Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Banco = models.CharField(max_length=20)
    NoCuenta = models.CharField(max_length=20)
    Monto = models.FloatField()
    Depositado = models.BooleanField(null=True, blank=True)
    Mensaje = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
