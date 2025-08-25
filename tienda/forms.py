from django import forms
from .models import Producto

class AgregarProductoForm(forms.ModelForm):
    tipo = forms.ChoiceField(label='Variedad:',
                        choices=Producto.TIPOS_NARANJA,
                        widget=forms.Select(
                            attrs={'class':'form'}
                        ))
    precio_por_kilo = forms.DecimalField(label='Precio por Kilo:',
                        widget=forms.NumberInput(
                            attrs={'class':'form', 'min':'0'}
                        ))
    kilos_disponibles = forms.IntegerField(label='Kilos Disponibles:',
                        widget=forms.NumberInput(
                            attrs={'class':'form', 'min':'1'}
                        ))
    class Meta:
        model = Producto
        fields = [
            'tipo',
            'precio_por_kilo',
            'kilos_disponibles',
        ]