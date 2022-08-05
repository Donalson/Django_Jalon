from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login/')
def index(request):
    usuario = {'username':'Donalson', 'category':'admin'}
    return render(request, 'Jalon/index.html', {'usuario':usuario})