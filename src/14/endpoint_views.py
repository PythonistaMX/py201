from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest

@csrf_exempt
def clave(request, clave):
    if request.method == "GET":
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave) 
            return JsonResponse({campo:getattr(alumno, campo) for campo in campos})
        except models.Alumno.DoesNotExist:
            return HttpResponseNotFound()
    if request.method == "POST":
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave) 
            return HttpResponseBadRequest()
        except models.Alumno.DoesNotExist:
            registro = request.POST.dict()
            registro["numero_de_cuenta"] = int(clave)
            objeto = models.Alumno()
            for campo in registro:
                setattr(objeto, campo, registro[campo])
            objeto.save()
            return JsonResponse(registro)
    if request.method == "DELETE":
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave)
            alumno.delete()
            return JsonResponse({'estado': 'eliminado'})
            
        except models.Alumno.DoesNotExist:
            return HttpResponseNotFound()