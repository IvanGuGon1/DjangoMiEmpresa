from django.db import models
from django.core.urlresolvers import reverse

class Clientes(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('clientes_edit', kwargs={'pk': self.pk})

class Proveedores(models.Model):
	nombre = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('proveedores_edit', kwargs={'pk': self.pk})


class Productos(models.Model):
	nombre = models.CharField(max_length=200)
	descripcion = models.CharField(max_length=200)
	precio = models.FloatField(max_length=200)
	stock = models.IntegerField()
	proveedor = models.ForeignKey(Proveedores)


	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('productos_edit', kwargs={'pk': self.pk})

class Pedidos(models.Model):
	descripcion = models.CharField(max_length=200)
	fecha = models.DateField()
	direccion = models.CharField(max_length=200)
	telefono = models.CharField(max_length=200)
	productos = models.ForeignKey(Productos)
	unidades = models.IntegerField()
	precioFinal = models.FloatField(default=0)
	clientes = models.ForeignKey(Clientes)

	def __str__(self):
		return self.descripcion

	def get_absolute_url(self):
		return reverse('pedidos_edit', kwargs={'pk': self.pk})
