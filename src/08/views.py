from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")


def calificaciones(request):
    return HttpResponse(request.method)


def clave(request, clave):
    return HttpResponse('<h1>Introdujiste la clave: {}</h1>'.format(str(clave)))


def numero(request, numero):
    return HttpResponse('<h1>Introdujiste el número: {}</h1>'.format(str(numero)))


def saluda(request, nombre):
    return HttpResponse('<h1>¡Hola, {}!</h1>'.format(nombre))