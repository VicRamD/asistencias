from django.urls import path
from .views import crearCuentaBancaria, personasConCuenta

app_name = 'persona'
urlpatterns = [
  #  path('crearPersona/',crearPersona,name='crearPrograma'),
    path('crearCuentaBancaria',crearCuentaBancaria,name='crearCuentaBancaria'),
    path('',personasConCuenta,name='listaCuentas'),
]
