from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.bienvenida, name='bienvenida'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('registrar/', views.registrar, name='registrar'),
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
]