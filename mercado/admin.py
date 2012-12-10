from django.contrib import admin
from models import *


class RegistroMercadoInline(admin.StackedInline):
	model = RegistroMercado
	extra = 1

class RegistroAdmin(admin.ModelAdmin):
	inlines = [RegistroMercadoInline]

admin.site.register(Registro, RegistroAdmin)
admin.site.register(RegistroMercado)
admin.site.register(PersonaContacto)
admin.site.register(TipoOrganizacion)
admin.site.register(Periodicidad)
admin.site.register(TiposOrganizacionesApoyan)
admin.site.register(ApoyanMercado)
admin.site.register(ProductosFrescos)
admin.site.register(ProductosProcesados)
admin.site.register(ActividadMercado)


class MovimientoProductosFrescoInline(admin.StackedInline):
	model = MovimientoProductosFresco
	extra = 1

class MovimientoProductosProcesadosInline(admin.StackedInline):
	model = MovimientoProductosProcesados
	extra = 1

class MovimientoAdmin(admin.ModelAdmin):
	date_hierarchy = 'fecha'
	list_display = ('nombre_mercado', 'nombre_persona', 'organizacion_persona',)
	list_filter = ('nombre_mercado',)
	inlines = [MovimientoProductosFrescoInline, 
	           MovimientoProductosProcesadosInline]

admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(MovimientoProductosFresco)
admin.site.register(MovimientoProductosProcesados)