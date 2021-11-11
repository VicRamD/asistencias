from django.contrib.auth.decorators import permission_required, login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
# Create your views here.
from apps.persona.forms import PersonaForm, CuentaBancariaForm
from apps.persona.models import CuentaBancaria

"""
def crearPersona(request):
    persona = None
    if request.method == 'POST':
        formPersona = PersonaForm(request.POST, request.FILES)
        if formPersona.is_valid():
            persona = formPersona.save(commit = True)
            return redirect(request, 'persona:#',args=persona)
"""

@permission_required('CuentaBancaria.add_CuentaBancaria')
def crearCuentaBancaria(request):
    nuevaCuenta = None
    if request.method == 'POST':
        formCuenta = CuentaBancariaForm(request.POST, request.FILES)
        if formCuenta.is_valid():
            nuevaCuenta = formCuenta.save(commit=True)
            return redirect(request, 'persona:crearCuentaBancaria', args={nuevaCuenta.numero_cuenta})
    else:
        formCuenta = CuentaBancariaForm()
    return render(request, 'crearCuenta.html',{'form': formCuenta})

#Requiere inicio de sesión
@login_required
def personasConCuenta(request):
    cuentasResgistradas = CuentaBancaria.objects.all().order('dni')
    return render(request, 'lista_cuentas.html',{'cuentasResgistradas':cuentasResgistradas})