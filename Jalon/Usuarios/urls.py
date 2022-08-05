from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='Usuarios'),
    path('usuario/<int:id>', views.usuario, name='Detalle'),
    path('verificacion/', views.verificacion, name='Verificacion')
]