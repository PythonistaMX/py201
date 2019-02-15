from django.http import HttpResponse, HttpResponseServerError, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")


def error(request):
    return HttpResponseServerError('¡Ups!')


def otro_error(request):
    return HttpResponseServerError(None)

@csrf_exempt
def contenido(request):
    return JsonResponse(request.POST.dict())