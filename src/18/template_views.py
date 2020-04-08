from .models import Alumno
from django.shortcuts import render

campos = ('numero_de_cuenta', 'nombre', 'primer_apellido', 'segundo_apellido', 'carrera', 'semestre', 'promedio', 'al_corriente')

def vista(request):
    lista = [[(campo, getattr(alumno, campo)) for campo in campos] for alumno in Alumno.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'listado.html', contexto) 

def valida(request):
    lista = [[getattr(alumno, campo) for campo in campos] for alumno in Alumno.objects.all()]
    contexto = {'lista': lista}
    return render(request, 'valida.html', contexto) 