from django.db import models
from accounts.models import Estudiante


class Entry(models.Model):
    """ Es la entrada de un foro """
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)

    ## agregar material
    ## agregar ramos

    def __str__(self):
        return self.title

class Message(models.Model):
    """ Es un mensaje en una entrada de un foro """
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    entry_id = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Mensaje en {self.entry_id}"