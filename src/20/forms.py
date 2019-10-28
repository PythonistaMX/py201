from django import forms

CARRERAS =(('Sistemas', 'Sistemas'), 
           ('Derecho', 'Derecho'), 
           ('Actuaría', 'Actuaría'),
           ('Arquitectura', 'Arquitectura'),
           ('Administración', 'Administración'))

class FormaAlumno(forms.Form):
    numero_de_cuenta = forms.IntegerField(label='Número de cuenta',
                                          min_value=1000, 
                                          max_value=9999,
                                          error_messages={'required': 'Dato requerido'})
    nombre = forms.CharField(max_length=50, 
                             label='Nombre')
    primer_apellido = forms.CharField(max_length=50, 
                                      label='Primer apellido')
    segundo_apellido = forms.CharField(max_length=50, 
                                       label='Segundo apellido', 
                                       required=False)
    carrera = forms.ChoiceField(label='Carrera', 
                                choices=CARRERAS)
    semestre = forms.IntegerField(label='Semestre', 
                                  min_value=1)
    promedio = forms.FloatField(label='Promedio',
                                min_value=0.,
                                max_value=10.0)   
    al_corriente = forms.BooleanField(required=False)