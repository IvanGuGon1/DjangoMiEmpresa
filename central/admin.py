from django.contrib import admin
from .models import Clientes, Proveedores, Productos, Pedidos

admin.site.register(Clientes)


admin.site.register(Proveedores)

admin.site.register(Productos)

admin.site.register(Pedidos)

