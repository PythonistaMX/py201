from . import models
from django.http import JsonResponse
import json

campos = {'numero_de_cuenta':int, 'nombre':str, 'primer_apellido':str,
          'segundo_apellido':str, 'carrera':str, 'semestre':int, 'promedio':float,
          'al_corriente':bool}

def carga(request):
    '''Función encargada de crear objetos instaciados de models.Alumno y de poblar la base de datos.'''
    # Carga los datos de un archivo JSON
    with open('alumnos.json', 'tr', encoding="utf-8") as archivo:
        alumnos = json.load(archivo)
    #Crea un objeto a partir de cada elemento tipo dict de alumnos
    for registro in alumnos:
        # Crea un objeto instanciando la clase Alumno
        objeto = models.Alumno()
        # Asigna cada campo a su atributo correspondiente
        for campo in registro:
            setattr(objeto, campo, registro[campo])
        # Guarda a la base dce datos.
        objeto.save()
    #Regresa la relaciónde alumnos dados de alta.
    return JsonResponse({'respuesta':alumnos})


def vista(request):
    return JsonResponse({'respuesta':[{campo:getattr(alumno, campo) for campo in campos} for alumno in models.Alumno.objects.all()]})