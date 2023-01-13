from django import forms
from django.contrib.auth.models import User
from Aplicaciones.Usuarios.models import PerfilUsuario
from Aplicaciones.Usuarios.choices import departamento

class formEnvio(forms.ModelForm):
    departamento =   forms.ChoiceField(label='Departamento',required=True, choices= departamento)
    ciudad =   forms.CharField(label='Ciudad',required=True,)
    direccion =   forms.CharField(label='Dirección',required=True,)
    celular =   forms.CharField(label='Celular',required=True,)
    cedula = forms.CharField(label='Cédula',required=True,)
    comentarios = forms.CharField(label='Notas',required=False,widget=forms.Textarea(attrs={'placeholder': 'Notas sobre tu pedido, por ejemplo, notas especiales para la entrega.','class': 'NotasEnvio'}))
    class Meta:
        model = PerfilUsuario
        fields = ['departamento','ciudad','direccion','celular','cedula','comentarios']