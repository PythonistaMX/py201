from . import models
from django.http import JsonResponse
import json

campos = {'numero_de_cuenta':int, 'nombre':str, 'primer_apellido':str,
          'segundo_apellido':str, 'carrera':str, 'semestre':int, 'promedio':float,
          'al_corriente':bool}

def carga(request):
    with open('alumnos.json', 'tr') as archivo:
        alumnos = json.load(archivo)
    for registro in alumnos:
        objeto = models.Alumno()
        for campo in registro:
            setattr(objeto, campo, registro[campo])
        objeto.save()
    return JsonResponse({'respuesta':alumnos})
  
    
def vista(request):
    return JsonResponse({'respuesta':[{campo:getattr(alumno, campo) for campo in campos} for alumno in models.Alumno.objects.all()]})