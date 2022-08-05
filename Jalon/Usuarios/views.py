from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario
# Create your views here.

@login_required(login_url='login/')
def usuarios(request):
    Usuarios = Usuario.objects.filter(Verificado=None)
    return render(request, 'Usuarios/usuarios.html', {'usuarios':Usuarios})

@login_required(login_url='login/')
def usuario(request, id):
    user = Usuario.objects.get(id=id)
    if(user.Verificado == None):
        return render(request, 'Usuarios/usuario.html', {'usuario':user})
    else:
        messages.warning(request, 'Parece que el usuario seleccionado ya ha sido clasificado')
        return redirect('Usuarios')

@login_required(login_url='login/')
def verificacion(request):

    if request.method == 'POST':
        user = request.POST['usuario']
        mensaje = request.POST['Mensaje']
        verifcado = int(request.POST['Verificado'])
        if verifcado == 0:
            displaymessage = 'Se ha denegado al usuario {}'.format(user)
            messages.error(request, displaymessage)
            datos = Usuario.objects.get(Usuario = user)
            datos.Verificado = False
            datos.Mensaje = mensaje
            datos.save()
            return redirect('Usuarios')
        elif verifcado == 1:
            displaymessage = 'Se ha aprobado al usuario {}'.format(user)
            messages.success(request, displaymessage)
            datos = Usuario.objects.get(Usuario = user)
            datos.Verificado = True
            datos.Mensaje = mensaje
            datos.save()
            return redirect('Usuarios')
        else:
            return redirect('Usuarios')