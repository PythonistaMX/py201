from django.urls import path, re_path
from . import views, endpoint_views, template_views

urlpatterns = [path('', views.vista),
               path('carga', views.carga),
               re_path(r'^(?P<clave>[0-9]{4}$)', endpoint_views.clave),
               path('vista/', template_views.vista),
               path('valida/', template_views.valida),
               path('alta/', template_views.forma),
         ]