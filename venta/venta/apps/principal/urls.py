
from django.conf.urls import patterns, include, url
from views import *
from django.conf import settings
urlpatterns = patterns('',
	url(r'^$',inicio),
	url(r'^nuevousuario$',nuevousuario),
	url(r'^ingresar$',ingresar),
	url(r'^cerrar$',cerrar),
	url(r'^regiscliente$',regiscliente),
	url(r'^clientes$',clientes),
	url(r'^index$',index),
	url(r'^index1$',inicio1),
	url(r'^index2$',inicio2),
	url(r'^index3$',inicio3),
	url(r'^reservass$',reservass),
	url(r'^clientesregis$',clientesregis),
	url(r'^galeria$',galeria),
	url(r'^sectors/(?P<id>\d+)$',sectors),
	url(r'^preferencias/(?P<id>\d+)$',preferencias),
	url(r'^generals/(?P<id>\d+)$',generals),
	url(r'^curvasur/(?P<id>\d+)$',curvasur),
	url(r'^curvanorte/(?P<id>\d+)$',curvanorte),
	url(r'^reservas/(?P<id>\d+)/$',reservacion),
	url(r'^desigpartido/$',desigpartido),
	url(r'^designarasiento$',designarasiento),
	url(r'^partidos$',partidos),
	url(r'^paypal/(?P<id>\d+)$',paypal),
	url(r'^venta',ventas_ent),
	url(r'^res_ent',res_ent),
	url(r'^reportres',reportres),

	url(r'^crear_reporte/(?P<id>\d+)$',crear_reporte),



	)