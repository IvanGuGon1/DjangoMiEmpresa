from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls import url

from central import views

urlpatterns = [

    url(r'^home/$', views.HomePageView.as_view(), name='home'),
	url(r'^proveedores/$', views.ProveedoresList.as_view(), name='proveedores_list'),
	url(r'^proveedores/new$', views.ProveedoresCreate.as_view(), name='proveedores_new'),
	url(r'^proveedores/edit/(?P<pk>\d+)$', views.ProveedoresUpdate.as_view(), name='proveedores_edit'),
	url(r'^proveedores/delete/(?P<pk>\d+)$', views.ProveedoresDelete.as_view(), name='proveedores_delete'),

	url(r'^clientes/$', views.ClientesList.as_view(), name='clientes_list'),
	url(r'^clientes/new$', views.ClientesCreate.as_view(), name='clientes_new'),
	url(r'^clientes/edit/(?P<pk>\d+)$', views.ClientesUpdate.as_view(), name='clientes_edit'),
	url(r'^clientes/delete/(?P<pk>\d+)$', views.ClientesUpdate.as_view(), name='clientes_delete'),

	url(r'^productos/$', views.ProductosList.as_view(), name='productos_list'),
	url(r'^productos/new$', views.ProductosCreate.as_view(), name='productos_new'),
	url(r'^productos/edit/(?P<pk>\d+)$', views.ProductosUpdate.as_view(), name='productos_edit'),
	url(r'^productos/delete/(?P<pk>\d+)$', views.ProductosDelete.as_view(), name='productos_delete'),

	url(r'^pedidos/$', views.PedidosList.as_view(), name='pedidos_list'),
	url(r'^pedidos/new$', views.PedidosCreate.as_view(), name='pedidos_new'),
	url(r'^pedidos/edit/(?P<pk>\d+)$', views.PedidosUpdate.as_view(), name='pedidos_edit'),
	url(r'^pedidos/delete/(?P<pk>\d+)$', views.PedidosDelete.as_view(), name='pedidos_delete'),

	]