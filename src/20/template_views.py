from .models import Alumno
from .forms import FormaAlumno
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, render_to_response
from requests import post

campos = ('numero_de_cuenta', 'nombre', 'primer_apellido', 'segundo_apellido', 'carrera', 'semestre', 'promedio', 'al_corriente')


def vista(request):
    lista = [[(campo, getattr(alumno, campo)) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('listado.html',{'lista': lista}) 


def valida(request):
    lista = [[getattr(alumno, campo) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('valida.html',{'lista': lista}) 

def forma(request):
    if request.method == 'POST':
        forma = FormaAlumno(request.POST)
        if forma.is_valid():
            datos = request.POST.dict()
            datos.pop('csrfmiddlewaretoken')
            cuenta = datos.pop('numero_de_cuenta')
            if 'al_corriente' in datos:
                datos['al_corriente']=True
            else:
                datos['al_corriente']=False
            resultado = post('http://' + request.get_host() + '/api/{}'.format(cuenta), data=datos)
            if resultado.status_code == 200:
                return HttpResponse('<h1>¡Alta Exitosa!</h1>')    
            else: 
                return HttpResponse('<h1>Ocurrió un error en el alta.</h1>')  
    else:
        forma = FormaAlumno()

    return render(request, 'forma.html', {'forma': forma}) 