from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response


def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")


def calificaciones(request):
    return HttpResponse(request.method)


def clave(request, clave):
    return HttpResponse('<h1>Introdujiste la clave: {}</h1>'.format(str(clave)))


def numero(request, numero):
    return HttpResponse('<h1>Introdujiste el número: {}</h1>'.format(str(numero)))


def saluda(request, nombre):
    return render_to_response('base.html', {"titulo":"Prueba de plantilla", "nombre": nombre})


def respuesta_json(request):
    
    return JsonResponse({'tipo contenido':request.content_type, 'metodo':request.method, 'ruta':request.path})