from django.conf.urls.defaults import *

urlpatterns = patterns('movimientos.views',
	url(r'^$', 'index', name="index"),
	url(r'^ver_mercado/(?P<id>\d+)/$', 'ver_mercado', name="vermercado"),
	url(r'^explora/$', 'explorar', name="explorar"),
	url(r'^explora/test/$', 'test_mapa', name="test_mapa"),
	url(r'^agregar/movimientos/$', 'multipleform', name="prueba"),
	url(r'^reqdata/$', 'reqdata', name="reqdata"),
	url(r'^traemelosdatos/$', 'mandar_info_producto', name="mandar-info-producto"),
	url(r'^traemelosdatosmas/$', 'mandar_info_procesado', name="mandar-info-procesado"),
	url(r'^mercado_mapa/$', 'mapa_mercado', name="mapa-mercado"),
	url(r'^ver_mapa_completo/$', 'mapa_completo', name="mapa-completo"),
	url(r'^ver_mapa/$', 'obtener_mapa', name="obtener-mapa"),
	url(r'^posicion_mapa/$', 'posicion_mapa', name="posicion-mapa"),
	url(r'^lista-mercados/$', 'lista_mercados', name="lista_mercados"),
	url(r'^registrate/$', 'registrar', name="registrar"),
)

