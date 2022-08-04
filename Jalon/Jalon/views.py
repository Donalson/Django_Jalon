from django.shortcuts import render

def index(request):
    usuario = {'username':'Donalson', 'category':'admin'}
    return render(request, 'Jalon/index.html', {'usuario':usuario})