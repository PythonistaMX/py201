from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")


def vista(request):
    return HttpResponse('<ul><li>URL: {}</li><li>Método: {}</li><li>Codificación: {}</li><li>Argumentos: {}</li></ul>'.format(request.path, request.method, request.encoding, request.GET.dict()))

def clave(request, clave):
    return HttpResponse('<h1>Ingresaste la clave: {}</h1>'.format(str(clave)))


def numero(request, numero):
    return HttpResponse('<h1>Ingresaste el número: {}</h1>'.format(str(numero)))


def saluda(request, nombre):
    return HttpResponse('<h1>¡Hola, {}!</h1>'.format(nombre))


def respuesta_json(request):
    return JsonResponse({'tipo contenido':request.content_type, 'metodo':request.method, 'ruta':request.path,  'argumentos':request.GET.dict()})