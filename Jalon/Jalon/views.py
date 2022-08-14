from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Usuarios.models import Usuario
from Depositos.models import Depositos

@login_required(login_url='Login', redirect_field_name='luego')
def index(request):
    Usuarios_Pedientes = len(Usuario.objects.filter(Verificado=None))
    Depositos_Pedientes = len(Depositos.objects.filter(Depositado=None))
    return render(request, 'Jalon/index.html', {'Usuarios':Usuarios_Pedientes, 'Depositos':Depositos_Pedientes})