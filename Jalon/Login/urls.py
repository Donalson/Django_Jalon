from django.urls import path

from Login import views

urlpatterns = [
    path('login/', views.login, name="Login"),
    path('verificacion/', views.verificacion, name='Verificacion'),
    path('registrar', views.registrar, name='Registrar'),
]