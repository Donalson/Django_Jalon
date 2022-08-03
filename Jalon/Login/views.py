from django.shortcuts import render, HttpResponse

# Funcion de vista para mostrar el formulario de inicio de sesion
def login(request):

    return render(request, 'Login/login.html', {})

# Funcion de vista para verificar que el usuario, contraseña y categoria conincidan con la api
def verificacion(request):

    return HttpResponse('Verificacion de URL')

# Funcion de vista por si se necesita registrar usuarios
def registrar(request):

    return HttpResponse('URL por si se necesita registrar usuarios')