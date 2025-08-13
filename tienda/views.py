from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def menu_tienda(request):
    return render(request, 'tienda/menu.html')