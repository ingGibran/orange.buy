from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_tienda, name='menu_tienda'),
    path('vender/', views.vender, name='vender'),
    path('mis_ventas/', views.mis_ventas, name='mis_ventas'),
    
    path('pausar/<int:venta_id>/', views.pausar_venta, name='pausar_venta'),
    path('reanudar/<int:venta_id>/', views.reanudar_venta, name='reanudar_venta'),
    path('eliminar/<int:venta_id>/', views.eliminar_venta, name='eliminar_venta'),
    
    path('cerrar_sesion/', views.cerrar_sesion, name='cerrar_sesion'),
    
    path('producto/<int:producto_id>/', views.producto, name='producto'),
]