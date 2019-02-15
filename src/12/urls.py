from django.urls import path, re_path 
from . import views

urlpatterns = [path('', views.index, name="inicio"),
               path('otro_error', views.otro_error),
               path('error', views.error),
               path('contenido', views.contenido),]