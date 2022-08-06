from django.urls import path
from . import views

urlpatterns = [
    path('depositos/', views.depositos, name='Depositos'),
    path('deposito/<int:id>', views.deposito, name='Deposito'),
    path('verificacion_deposito/', views.verificacion_deposito, name='Verificacion_Deposito'),
]