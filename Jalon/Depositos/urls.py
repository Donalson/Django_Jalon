from django.urls import path
from . import views

urlpatterns = [
    path('depositos/', views.usuarios, name='Depositos'),
    path('deposito/<int:id>', views.usuario, name='Deposito'),
    path('verificacion_deposito/', views.verificacion, name='Verificacion_Deposito')
]