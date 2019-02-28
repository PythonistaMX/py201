

from django.forms import Form

class FormaAlumno(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

