from django import forms
from forum.models import Entry, Message

"""
Formulario para agregar entrada de un foro
Tiene:
    (1) Titulo: titulo de la entrada
    (2) Cuerpo: mensaje de la entrada
"""
class ForumEntry(forms.ModelForm): #username, password, email, nombre, apellido

    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=1000)
    
    class Meta:
        model = Entry
        fields = ['title', 'body']

""" 
Formulario para agregar mensaje a un foro 
Tiene:
    (1) Mensaje: mensaje enviado
"""
class ForumMessage(forms.ModelForm): #username, password, email, nombre, apellido
    message = forms.CharField(max_length=1000)
    
    class Meta:
        model = Message
        fields = ['message']