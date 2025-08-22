from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AgregarProductoForm
from .models import Producto, Producto

# Create your views here.

@login_required
def menu_tienda(request):
    valencia = Producto.objects.filter(activo=True, tipo='valencia')
    navel = Producto.objects.filter(activo=True, tipo='navel')
    sanguinea = Producto.objects.filter(activo=True, tipo='sanguinea')
    otra = Producto.objects.filter(activo=True, tipo='otra')
    return render(request, 'tienda/menu.html', {'valencia':valencia, 'navel':navel, 'sanguinea': sanguinea, 'otra':otra})

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

@login_required
def pausar_venta(request, venta_id):
    producto = get_object_or_404(Producto, id=venta_id, vendedor=request.user)
    producto.activo = False
    producto.save()
    return redirect('mis_ventas')

@login_required
def reanudar_venta(request, venta_id):
    producto = get_object_or_404(Producto, id=venta_id, vendedor=request.user)
    producto.activo = True
    producto.save()
    return redirect('mis_ventas')

@login_required
def eliminar_venta(request, venta_id):
    producto = get_object_or_404(Producto, id=venta_id, vendedor=request.user)
    producto.delete()
    return redirect('mis_ventas')
    