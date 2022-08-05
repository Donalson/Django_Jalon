from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.models import Usuario
# Create your views here.

@login_required(login_url='login/')
def usuarios(request):
    Usuarios = Usuario.objects.filter(Verificado=0)
    return render(request, 'Usuarios/usuarios.html', {'usuarios':Usuarios})

@login_required(login_url='login/')
def usuario(request, id):
    user = Usuario.objects.filter(id=id)
    return render(request, 'Usuarios/usuario.html', {'usuario':user})
