from .models import Alumno
from .forms import FromaAlumno
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

campos = ('numero_de_cuenta', 'nombre', 'primer_apellido', 'segundo_apellido', 'carrera', 'semestre', 'promedio', 'al_corriente')


def vista(request):
    lista = [[(campo, getattr(alumno, campo)) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('listado.html',{'lista': lista}) 


def valida(request):
    lista = [[getattr(alumno, campo) for campo in campos] for alumno in Alumno.objects.all()]
    return render_to_response('valida.html',{'lista': lista}) 

def forma(request):
   # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        forma = FormaAlumno(request.POST)
        # check whether it's valid:
        if forma.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        forma = FormaAlumno()

    return render(request, 'forma.html', {'forma': forma}) 