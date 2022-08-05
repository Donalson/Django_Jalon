from django.urls import path
from Usuarios import views

urlpatterns = [
    path('usuarios/', views.usuarios, name='Usuarios'),
    path('usuario/<int:id>', views.usuario),
]