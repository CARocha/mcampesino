from django.conf.urls.defaults import *

urlpatterns = patterns('mercado.views',
	url(r'^$', 'index', name="index"),
	url(r'^ver_mercado/(?P<id>\d+)/$', 'ver_mercado', name="vermercado"),
	url(r'^explora/$', 'explorar', name="explorar"),
	url(r'^prueba/$', 'multipleform', name="prueba"),
	url(r'^reqdata/$', 'reqdata', name="reqdata"),

)

