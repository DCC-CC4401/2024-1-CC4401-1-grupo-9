from django.db import models


class Course(models.Model):
    """ Course: 
            Representa los Ramos disponibles
        - name: Nombre del ramo
    """
    name  = models.CharField(max_length=50)


class Material(models.Model):
    """ Material:
            Representa los materiales disponibles
        - name: nombre del material
        - path: ruta del archivo
        - course: Ramo del material
    """
    name  = models.CharField(max_length=50)
    path  = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
