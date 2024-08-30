from django.shortcuts import render, redirect
from .forms import CategoriaForm, ProductoForm, ClienteForm, BuscarProductoForm
from .models import Producto

def agregar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CategoriaForm()
    return render(request, 'mi_app/agregar_categoria.html', {'form': form})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProductoForm()
    return render(request, 'mi_app/agregar_producto.html', {'form': form})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'mi_app/agregar_cliente.html', {'form': form})

def buscar_producto(request):
    form = BuscarProductoForm()
    productos = []
    if request.method == 'GET':
        nombre = request.GET.get('nombre')
        if nombre:
            productos = Producto.objects.filter(nombre__icontains=nombre)
    return render(request, 'mi_app/buscar_producto.html', {'form': form, 'productos': productos})

def index(request):
    return render(request, 'mi_app/index.html')
