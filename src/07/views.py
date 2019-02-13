from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")

def calificaciones(request):
    return HttpResponse(request.method)