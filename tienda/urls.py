from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_tienda, name='menu_tienda'),
    path('vender/', views.vender, name='vender'),
    path('mis_ventas/', views.mis_ventas, name='mis_ventas')
]