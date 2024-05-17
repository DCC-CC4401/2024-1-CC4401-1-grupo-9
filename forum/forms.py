from django import forms
from forum.models import Entry, Message

class ForumEntry(forms.Form): #username, password, email, nombre, apellido
    """ Formulario para agregar entrada de un foro """

    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=1000)
    
    class Meta:
        model = Entry
        fields = ['title', 'body']

class ForumMessage(forms.Form): #username, password, email, nombre, apellido
    """ Formulario para agregar mensaje a un foro """
    message = forms.CharField(max_length=1000)
    
    class Meta:
        model = Message
        fields = ['message']