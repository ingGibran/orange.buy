from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class RegistroForm(UserCreationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Nombre de Usuario'
        })
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Correo Electrónico'
        })
    )
    password1 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Contraseña'
        })
    )
    password2 = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Repetir Contraseña'
        })
    )
    class Meta:
        model = User
        fields = ['username', 'email' ,'password1', 'password2']


class LoginForn(AuthenticationForm):
    username = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Nombre de Usuario'
        })
    )
    password = forms.CharField(
        max_length=100,
        widget=forms.PasswordInput(attrs={
            'class': 'form-registro',
            'placeholder': 'Contraseña'
        })
    )
    class Meta:
        model = User
        fields = ['username','password']