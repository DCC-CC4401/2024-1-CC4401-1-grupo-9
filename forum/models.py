from django.db import models
from django.contrib.auth.models import User
from accounts.models import Estudiante

"""
Entrada de un foro, representa las publicaciones realizadas por los estudiantes en el foro.
La entrada de un foro posee:
    (1) Titulo: Titulo de la entrada 
    (2) Cuerpo: Mensaje de la entrada
    (3) Usuario: Estudiante que realiza la entrada
    (4) Fecha: Fecha de creacion de la entrada
"""
class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=1000)
    user = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    ## agregar material
    ## agregar ramos

    def __str__(self):
        return self.title

"""
Mensaje de un foro, se utiliza para almacenar los comentarios realizados por los usuarios en respuesta
a las entradas del foro.
El mensaje de un foro tiene:
    (1) Mensaje: Mensaje que se quiere subir
    (2) Entrada: Entrada a la que se le hace referencia o se responde.
    (3) Usuario: Estudiante que realiza el mensaje
    (4) Fecha: Fecha de creacion de el mensaje
"""
class Message(models.Model):
    message = models.TextField(max_length=1000)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    user = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje en {self.entry_id}"