from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Roles(models.Model):
    name = models.CharField()
    description = models.CharField()

    def __str__(self):
        return self.name

class Estudiante(AbstractUser):
    total_answers = models.IntegerField()
    useful_answers = models.IntegerField()
    total_questions = models.IntegerField()
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)
    #puntaje = 3 *total_answers + 5 * useful_answers + 2 * total_questions #Revisar

    def __str__(self):
        return self.first_name +" "+ self.last_name