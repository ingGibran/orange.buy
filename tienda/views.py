from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AgregarProductoForm
from .models import Producto

# Create your views here.

@login_required
def menu_tienda(request):
    return render(request, 'tienda/menu.html')

@login_required
def vender(request):
    if request.method == 'POST':
        form = AgregarProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.vendedor = request.user
            producto.save()
            return redirect('mis_ventas')
    else:
        form = AgregarProductoForm()
    
    return render(request, 'tienda/vender.html', {'form':form})

@login_required
def mis_ventas(request):
    ventas = Producto.objects.filter(vendedor=request.user)
    return render(request, 'tienda/mis_ventas.html', {'ventas':ventas})