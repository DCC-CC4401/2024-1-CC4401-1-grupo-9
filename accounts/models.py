from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

"""
Clase estudiante

Representa a un estudiante de la FCFM

Atributos:
    username: nombre de usuario del estudiante
    password: contraseña del estudiante
    first__name: primer nombre del estudiante
    las_name: apellido del estudiante
    email: correo de contacto del estudiante
    total_answers: total de preguntas respondidas en un foro
    useful_answers: total de preguntas respondidas de forma útil (alguien reportó que su respuesta 
    sirvió)
    total_questions: total de preguntas realizadas
    groups: rol que cumple en la aplicacion
    user_permissions: permisos que tiene este usuario

De momento cada estudiante puede:
    1) Acceder a Mechón Pautero
    2) Acceder a su perfil de Mechón Pautero
    3) Acceder al perfil de otros usuarios de Mechón Pautero
    3) Postear entradas en el foro de la Mechón Pautero
    4) Revisar las entradas del foro de la Mechón Pautero
"""
class Estudiante(AbstractUser):
    total_answers = models.IntegerField(default=0)
    useful_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name='estudiante_groups')  # Añade related_name
    user_permissions = models.ManyToManyField(Permission, related_name='estudiante_user_permissions')  # Añade related_name

    def __str__(self):
        return self.first_name +" "+ self.last_name