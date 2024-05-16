from django.db import models
from accounts.models import User


class Entry(models.Model):
    """ Es la entrada de un foro """
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    ## agregar material
    ## agregar ramos

    def __str__(self):
        return self.title

class Message(models.Model):
    """ Es un mensaje en una entrada de un foro """
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    entry_id = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name