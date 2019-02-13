from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")

def calificaciones(request):
    pass