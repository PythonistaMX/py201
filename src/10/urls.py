from django.urls import path, re_path 
from . import views


urlpatterns = [path('', views.index, name="inicio"), 
               path('calif', views.calificaciones),
               re_path(r'^claves/(?P<clave>[0-9]{4}$)', views.clave),
               path('claves/<int:numero>', views.numero),
               path('claves/<str:nombre>', views.saluda),
               path('json', views.respuesta_json),
               path('otro_error', views.otro_error),
               path('error', views.error),
               path('contenido', views.contenido),]