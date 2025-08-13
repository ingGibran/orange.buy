from django.urls import path
from . import views

urlpatterns = [
    path('menu/', views.menu_tienda, name='menu_tienda'),
]