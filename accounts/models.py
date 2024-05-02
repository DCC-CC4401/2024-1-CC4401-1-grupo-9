from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.


class Roles(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Estudiante(AbstractUser):
    total_answers = models.IntegerField()
    useful_answers = models.IntegerField()
    total_questions = models.IntegerField()
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Group, related_name='estudiante_groups')  # Añade related_name
    user_permissions = models.ManyToManyField(Permission, related_name='estudiante_user_permissions')  # Añade related_name
    #puntaje = 3 *total_answers + 5 * useful_answers + 2 * total_questions #Revisar

    def __str__(self):
        return self.first_name +" "+ self.last_name