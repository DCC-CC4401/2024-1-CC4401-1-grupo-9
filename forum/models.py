from django.db import models
from django.contrib.auth.models import User


class Entry(models.Model):
    """ Es la entrada de un foro """
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    ## agregar material
    ## agregar ramos

    def __str__(self):
        return self.title

class Message(models.Model):
    """ Es un mensaje en una entrada de un foro """
    message = models.TextField(max_length=1000)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje en {self.entry_id}"