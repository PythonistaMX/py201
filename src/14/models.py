from django.db import models

class Alumno(models.Model):
    numero_de_cuenta = models.PositiveIntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    primer_apellido = models.CharField(max_length=50)
    segundo_apellido = models.CharField(max_length=50)
    carrera = models.CharField(max_length=20)
    semestre = models.PositiveIntegerField(default=0)
    promedio = models.FloatField(default=0)
    al_corriente = models.BooleanField(default=True)