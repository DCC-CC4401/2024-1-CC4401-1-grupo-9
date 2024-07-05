from django.db import models


class Course(models.Model):
    """ Course: 
            Representa los Ramos disponibles
        - name: Nombre del ramo
    """
    name  = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Material(models.Model):
    """ Material:
            Representa los materiales disponibles
        - name: nombre del material
        - path: ruta del archivo
        - course: Ramo del material
    """
    name  = models.CharField(max_length=50)
    file  = models.FileField(upload_to='material/static/Documents')
    image = models.ImageField(upload_to='material/static/Documents', blank=True, null=True)

    # Filtros
    MATERIAL_TYPE_CHOICES = [
        ('Auxiliar', 'Auxiliar'),
        ('Control', 'Control'),
        ('Tutoría', 'Tutoría'),
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    type = models.CharField(max_length=50, choices=MATERIAL_TYPE_CHOICES, default='Material')
    year = models.IntegerField(default=1999)


    def __str__(self) -> str:
        return self.name
