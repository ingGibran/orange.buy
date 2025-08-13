from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegistroForm, LoginForn

# Create your views here.
def bienvenida(request):
    return render(request, 'manager/bienvenida.html')

def registrar(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
        else:
            return render(request, 'manager/registrar.html', {'form': form})
    else:
        form = RegistroForm()
        
    return render(request, 'manager/registrar.html', {'form':form})


def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForn(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('menu_tienda')
    else:
        form = LoginForn()
    return render(request, 'manager/iniciar_sesion.html', {'form':form})

def cerrar_sesion(request):
    logout(request)
    return redirect('bienvenida')

def menu(request):
    return render(request, 'manager/menu.html')