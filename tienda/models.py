from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Producto(models.Model):
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ventas')
    precio_por_kilo = models.DecimalField(max_digits=6, decimal_places=2)
    kilos_disponibles = models.PositiveIntegerField()
    fecha_inicio = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)

    TIPOS_NARANJA = [
        ("valencia", "Valencia"),
        ("navel", "Navel"),
        ("sanguina", "Sanguina"),
        ("otra", "Otra variedad"),
    ]
    tipo = models.CharField(max_length=20, choices=TIPOS_NARANJA)
    
    def __str__(self):
        return f"{self.tipo} - {self.precio_por_kilo} -{self.vendedor}"