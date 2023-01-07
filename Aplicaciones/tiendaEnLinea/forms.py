from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Aplicaciones.Usuarios.models import PerfilUsuario
from .models import comentariosProductos
from Aplicaciones.Usuarios.choices import departamento


class UserRegisterForm (UserCreationForm):
    nombre1 = forms.CharField(label='Primer nombre',required=False,)
    nombre2 = forms.CharField(label='Segundo nombre',required=False,)
    primerApellido = forms.CharField(label='Primer apellido',required=False,)
    segundoApellido = forms.CharField(label='Segundo apellido',required=False,)
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}
        
    class form2(forms.ModelForm):
        model = PerfilUsuario
        fields = ['nombre1']



from django.contrib.auth.forms import AuthenticationForm

class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'input__form'
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
        self.fields['password'].widget.attrs['class'] = 'input__form'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class editarDatos(forms.ModelForm):
    nombre1 =           forms.CharField(label='Primer Nombre',required=False,)
    nombre2 =           forms.CharField(label='Segundo Nombre',required=False,)
    primerApellido =    forms.CharField(label='Primer Apellido',required=False,)
    segundoApellido =   forms.CharField(label='Segundo Apellido',required=False,)
    departamento =   forms.ChoiceField(label='Departamento',required=False, choices= departamento)
    ciudad =   forms.CharField(label='Ciudad',required=False,)
    direccion =   forms.CharField(label='Dirección',required=False,)
    celular =   forms.CharField(label='Celular',required=False,)

    
    class Meta:
        model = PerfilUsuario
        fields = ['nombre1','nombre2','primerApellido','segundoApellido','departamento','ciudad','direccion','celular']



class formComentario(forms.ModelForm):
    comentario = forms.CharField(label='',required=True,widget=forms.TextInput(attrs={'placeholder': 'Escribe tu comentario...','class': 'opinionInput'}))

    class Meta:
        model = comentariosProductos
        fields = ['comentario']

