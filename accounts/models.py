from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class Estudiante(AbstractUser):
    total_answers = models.IntegerField(default=0)
    useful_answers = models.IntegerField(default=0)
    total_questions = models.IntegerField(default=0)
    groups = models.ManyToManyField(Group, related_name='estudiante_groups')  # Añade related_name
    user_permissions = models.ManyToManyField(Permission, related_name='estudiante_user_permissions')  # Añade related_name
    #puntaje = 3 *total_answers + 5 * useful_answers + 2 * total_questions #Revisar

    def __str__(self):
        return self.first_name +" "+ self.last_name