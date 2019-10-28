from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest

# campos define la estructura de los datos que va transmitir el servidor, incluyendo el tipo de dato y si es obligatorio.
campos = {'numero_de_cuenta':(int, True), 'nombre':(str, True), 'primer_apellido':(str, True),
          'segundo_apellido':(str, False), 'carrera':(str, True), 'semestre':(int, True),
          'promedio':(float, True), 'al_corriente':(bool, True)}

# carreras define la carrera que puede tener un alumno.
carreras = ('Sistemas', 'Derecho', 'Actuaría', 'Arquitectura', 'Administración')

# estructura base ci=ontiene un conjunto de los identificadores de campos. 
estructura_base = set(campos)

# Reglas de negocio.

def reglas(valor, campo):
    if campo == "carrera" and valor not in carreras:
        return False
    elif campo == "semestre" and valor < 1:
        return False
    elif campo == "promedio" and (valor < 0 or valor > 10):
        return False
    elif (campo in ("nombre", "primer_apellido") and (valor == "")):
        return False
    else:
        return True         

# Valida que el dato sea del tipo del campo correspondiente y en caso de quen así sea, llama a reglas(). 
def valida(dato, campo):
    tipo = campos[campo][0]
    try:
        if tipo is str:
            valor = dato
        elif tipo is float:
            valor = float(dato)
        else:
            valor = eval(dato)
        if type(valor) is tipo:
            return reglas(valor, campo)
        else:
            return False
    except:
        return False


@csrf_exempt
def clave(request, clave):
    '''Función de vista que define un endpoint correspondiente a una clave de 4 dígitos.
    Opera con los métodos GET, POST, DELETE.'''
    # Cuando la petición es GET va a obtener los datos del alumno con la clave correrspondiente.
    if request.method == "GET":
        # Esta operación se realiza en caso de que exista un objeto con el número de cuenta.
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave) 
            return JsonResponse({campo:getattr(alumno, campo) for campo in campos})
        # La excepción models.Alumno.DoesNotExist se desencadena cuando la búsqueda no arroje un resultado.
        except models.Alumno.DoesNotExist:
            return HttpResponseNotFound()
        
    # Cuando la petición es DELETE el alumno es eliminado de la base de datos.
    if request.method == "DELETE":
        # Esta operación se realiza en caso de que exista un objeto con el número de cuenta.
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave)
            alumno.delete()
            return JsonResponse({'estado': 'eliminado'})   
        except models.Alumno.DoesNotExist:
            return HttpResponseNotFound()
    # Cuando la petición es POST va a dar de alta los datos del alumno con la clave correspondiente y los datos enviados.
    
    if request.method == "POST":
        # Esta operación se realiza en caso de que no exista un objeto con el número de cuenta.
        try:
            alumno = models.Alumno.objects.get(numero_de_cuenta=clave) 
            return HttpResponseBadRequest()
        except models.Alumno.DoesNotExist:
            registro = request.POST.dict()
            registro["numero_de_cuenta"] = clave
            objeto = models.Alumno()
            estructura_registro = set(registro)
            if estructura_registro.issubset(estructura_base):
                for campo in estructura_base:
                    if campo not in estructura_registro:
                        if campos[campo][1]:
                            return HttpResponseBadRequest()
                        else:
                            registro[campo] = ''
                    tipo = campos[campo][0]
                    if valida(registro[campo], campo):
                        if tipo is not str:
                            valor = (eval(registro[campo]))
                        else:
                            valor = registro[campo]
                        setattr(objeto, campo, valor)
                    else:
                        return HttpResponseBadRequest()
                objeto.save()
                return JsonResponse(registro)
            else:
                return HttpResponseBadRequest()
            