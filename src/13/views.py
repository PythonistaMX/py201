from . import models
from django.http import JsonResponse
import json

def carga(request):
    with open('alumnos.json', 'tr') as archivo:
        alumnos = json.load(archivo)
    for registro in alumnos:
        objeto = models.Alumno()
        for campo in registro:
            setattr(objeto, campo, registro[campo])
        objeto.save()
    return JsonResponse({'respuesta':alumnos})
    