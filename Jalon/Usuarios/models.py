from django.db import models

# Create your models here.

class Usuario(models.Model):
    Usuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Categoria = models.IntegerField(blank=True, null=True)
    Usuario_FK = models.IntegerField(blank=True, null=True)
    Nombre_Completo = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=10, blank=True, null=True)
    Foto = models.ImageField()
    Verificado = models.BooleanField(default=False)
    Pose1 = models.ImageField()
    Pose2 = models.ImageField()
    Selfie1 = models.ImageField()
    Selfie2 = models.ImageField()
    Dpi = models.ImageField()
    Mensaje = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)