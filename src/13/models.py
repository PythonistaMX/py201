from django.db import models

class Alumno(models.Model):
    numero_de_cuenta = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    carrera = models.CharField(max_length=20)
    promedio = models.FloatField()
    al_corriente = models.BooleanField()