from django import forms
from forum.models import Entry, Message

class ForumEntry(forms.Form): #username, password, email, nombre, apellido

    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=1000)
    
    class Meta:
        model = Entry
        fields = ['title', 'body']