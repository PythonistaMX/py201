from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hola, mundo.</h1>")

def vista(request):
    return HttpResponse('<ul><li>URL: {}</li><li>Método: {}</li>, <li>Codificación; {}</li></ul>'.format(request.url,
                        request.method, request.encoding))