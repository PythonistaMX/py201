from django.urls import path, re_path
from . import views, endpoint_views

urlpatterns = [path('', views.vista),
               path('carga', views.carga),
               re_path(r'^(?P<clave>[0-9]{4}$)', endpoint_views.clave),
         ]