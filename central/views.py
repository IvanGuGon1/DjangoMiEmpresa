from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Clientes, Proveedores, Productos, Pedidos

from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"

class ClientesList(ListView):
    model = Clientes

class ClientesCreate(CreateView):
    model = Clientes
    success_url = reverse_lazy('clientes_list')
    fields = ['nombre', 'direccion', 'telefono']

class ClientesUpdate(UpdateView):
    model = Clientes
    success_url = reverse_lazy('clientes_list')
    fields = ['nombre', 'direccion', 'telefono']

class ClientesDelete(DeleteView):
    model = Clientes
    success_url = reverse_lazy('clientes_list')


class ProveedoresList(ListView):
    model = Proveedores

class ProveedoresCreate(CreateView):
    model = Proveedores
    success_url = reverse_lazy('proveedores_list')
    fields = ['nombre', 'direccion', 'telefono']

class ProveedoresUpdate(UpdateView):
    model = Proveedores
    success_url = reverse_lazy('proveedores_list')
    fields = ['nombre', 'direccion', 'telefono']

class ProveedoresDelete(DeleteView):
    model = Proveedores
    success_url = reverse_lazy('proveedores_list')



class ProductosList(ListView):
    model = Productos

class ProductosCreate(CreateView):
    model = Productos
    success_url = reverse_lazy('productos_list')
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

class ProductosUpdate(UpdateView):
    model = Productos
    success_url = reverse_lazy('productos_list')
    fields = ['nombre', 'descripcion', 'precio', 'stock', 'proveedor']

class ProductosDelete(DeleteView):
    model = Productos
    success_url = reverse_lazy('productos_list')


class PedidosList(ListView):
    model = Pedidos

class PedidosCreate(CreateView):
    model = Pedidos
    success_url = reverse_lazy('pedidos_list')
    fields = ['descripcion', 'fecha', 'direccion', 'telefono', 'productos', 'unidades', 'clientes']

class PedidosUpdate(UpdateView):
    model = Pedidos
    success_url = reverse_lazy('pedidos_list')
    fields = ['descripcion', 'fecha', 'direccion', 'telefono', 'productos', 'unidades', 'clientes']

class PedidosDelete(DeleteView):
    model = Pedidos
    success_url = reverse_lazy('pedidos_list')
    fields = ['descripcion', 'fecha', 'direccion', 'telefono', 'productos', 'unidades', 'clientes']