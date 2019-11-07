from django.http import HttpResponse, HttpResponseServerError, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")


def vista(request):
    return HttpResponse('<ul><li>URL: {}</li><li>Método: {}</li><li>Codificación: {}</li><li>Argumentos: {}</li></ul>'.format(request.path, request.method, request.encoding, request.GET.dict()))


def clave(request, clave):
    return HttpResponse('<h1>Introdujiste la clave: {}</h1>'.format(str(clave)))


def numero(request, numero):
    return HttpResponse('<h1>Introdujiste el número: {}</h1>'.format(str(numero)))


def saluda(request, nombre):
    return HttpResponse('<h1>¡Hola, {}!</h1>'.format(nombre))


def respuesta_json(request):
    return JsonResponse({'tipo contenido':request.content_type, 'metodo':request.method, 'ruta':request.path})


def error(request):
    return HttpResponseServerError('<h1>¡Ups!</h1>')


@csrf_exempt
def contenido(request):
    return JsonResponse(request.POST.dict())


def listas (request):
    return HttpResponse(request.GET.lists())