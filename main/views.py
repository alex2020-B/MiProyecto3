from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.

def homepage(request):
    return render(request, "main/inicio.html", {"productos": Producto.objects.all})


