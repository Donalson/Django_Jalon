from distutils.command.upload import upload
from django.db import models

# Create your models here.

def ruta_personalizada_foto(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Foto.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

def ruta_personalizada_Dpi(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Dpi.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

def ruta_personalizada_P1(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Pose1.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

def ruta_personalizada_P2(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Pose2.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

def ruta_personalizada_S1(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Selfie1.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

def ruta_personalizada_S2(instance, filename):
    ext = filename.split('.')[-1]
    Foto = 'Selfie2.{}'.format(ext)
    return 'usuario_{0}/{1}'.format(instance.id, Foto)

class Usuario(models.Model):
    Usuario = models.CharField(max_length=50)
    Contraseña = models.CharField(max_length=50)
    Categoria = models.IntegerField(blank=True, null=True)
    Usuario_FK = models.IntegerField(blank=True, null=True)
    Nombre_Completo = models.CharField(max_length=50)
    Telefono = models.CharField(max_length=10, blank=True, null=True,)
    Foto = models.ImageField(upload_to=ruta_personalizada_foto, null=True, blank=True)
    Verificado = models.BooleanField(default=False)
    Pose1 = models.ImageField(upload_to=ruta_personalizada_P1, null=True, blank=True)
    Pose2 = models.ImageField(upload_to=ruta_personalizada_P2, null=True, blank=True)
    Selfie1 = models.ImageField(upload_to=models.ImageField(upload_to=ruta_personalizada_S1, null=True, blank=True), null=True, blank=True)
    Selfie2 = models.ImageField(upload_to=ruta_personalizada_S2, null=True, blank=True)
    Dpi = models.ImageField(upload_to=ruta_personalizada_Dpi, null=True, blank=True)
    Mensaje = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)