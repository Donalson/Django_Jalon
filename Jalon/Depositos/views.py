from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Depositos
# Create your views here.

@login_required(login_url='login/')
def depositos(request):
    DepositosLista = Depositos.objects.filter(Depositado=None)
    return render(request, 'Depositos/depositos.html', {'depositos':DepositosLista})

@login_required(login_url='login/')
def deposito(request, id):
    deposito = Depositos.objects.get(id=id)
    if(deposito.Depositado == None):
        return render(request, 'Depositos/deposito.html', {'Deposito':deposito})
    else:
        messages.warning(request, 'Parece que el deposito seleccionado ya ha sido clasificado')
        return redirect('Depositos')

@login_required(login_url='login/')
def verificacion_deposito(request):

    if request.method == 'POST':
        id = request.POST['id']
        user = request.POST['user']
        mensaje = request.POST['Mensaje']
        depositado = int(request.POST['Depositado'])
        if depositado == 0:
            displaymessage = 'Deposito fallido al usuario {}'.format(user)
            messages.error(request, displaymessage)
            dato = Depositos.objects.get(id = id)
            dato.Depositado = False
            dato.Mensaje = mensaje
            dato.save()
            return redirect('Depositos')
        elif depositado == 1:
            displaymessage = 'Se ha aprobado el deposito al usuario {}'.format(user)
            messages.success(request, displaymessage)
            dato = Depositos.objects.get(id = id)
            dato.Depositado = True
            dato.Mensaje = mensaje
            dato.save()
            return redirect('Depositos')
        else:
            return redirect('Depositos')