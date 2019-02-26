from .models import Alumno
from django.shortcuts import render_to_response

campos = ('numero_de_cuenta', 'nombre', 'primer_apellido', 'segundo_apellido', 'carrera', 'semestre', 'promedio', 'al_corriente')

def vista(request):
    lista = [[(campo, getattr(alumno, campo)) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('listado.html',{'lista': lista}) 

def valida(request):
    lista = [[getattr(alumno, campo) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('valida.html',{'lista': lista}) 