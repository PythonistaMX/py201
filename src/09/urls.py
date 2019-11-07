from django.urls import path, re_path 
from . import views


urlpatterns = [path('', views.index, name="inicio"), 
               path('vista', views.vista),
               re_path(r'^claves/(?P<clave>[0-9]{4}$)', views.clave),
               path('claves/<int:numero>', views.numero),
               path('claves/<str:nombre>', views.saluda),
               path('json', views.respuesta_json),
               path('contenido', views.contenido),
               path('error', views.error),
               path('listas', views.listas)]