from django import forms
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class Register(UserCreationForm): #username, password, email, nombre, apellido
    username_r = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password_r = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    email_r = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    first_name_r = forms.CharField(max_length=30, label='Nombre', widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name_r = forms.CharField(max_length=30, label='Apellido', widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))


class ForgetPassword(forms.Form):
    username_l = forms.CharField(label='Username', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
