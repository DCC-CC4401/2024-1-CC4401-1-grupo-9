from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import Estudiante

"""
Formulario de ingreso de credenciales de la aplicación
"""
class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

"""
Formulario de Registro de la aplicación
"""
class Register(UserCreationForm): #username, password, email, nombre, apellido
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    #password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(max_length=30, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))
    class Meta:
        model = Estudiante
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
"""
Formulario de ayuda por perdida de contraseña

(Implementación final a futuro)
"""
class ForgetPassword(forms.Form):
    username_l = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
