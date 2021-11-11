from django import forms
from django.forms import DateInput

from apps.persona.models import CuentaBancaria, Persona


class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = ('numero_cuenta','cbu','alias','banco_emisor')


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ('dni', 'nombre_completo', 'fecha_nacimiento', 'sexo', 'domicilio')

        widgets = {
            'fecha_nacimiento': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
