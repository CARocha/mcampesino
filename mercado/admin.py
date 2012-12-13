from django.contrib import admin
from autocomplete.widgets import *
from mercado.models import *
from mercado.forms import *


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

class ActividadMercadoAdmin(admin.ModelAdmin):
	form = ActividadForm
	fieldsets = (
        (None, {
            'fields': (('fkmercado', 'fecha_actividad'),)
        }),
        (None, {
            'fields': ('direccion', ('persona_contacto', 'telefono', 'correo', 'pagina_url'),
                       ('tipo_organizacion_mercado','modalidad','periodicidad'),
                       ('vendedor_hombre','vendedor_mujer'),('comprador_hombre','comprador_mujer'),
                       ('abastecen_hombre','abastecen_mujer'),
                       ('apoyan_mercado','productos_frescos','productos_procesados'))
        }),
        )
	class Media:
		css = {
            'all': ('/files/css/chosen.css',),
       	}
		js = ('/files/js/jquery.min.js','/files/js/chosen.jquery.js','/files/js/pimp.js',)


admin.site.register(ActividadMercado, ActividadMercadoAdmin)


class MovimientoProductosFrescoInline(admin.StackedInline):
    model = MovimientoProductosFresco
    fieldsets = (
            (None, {
                'fields': ((('producto_fresco'),
                ('volumen_venta_global','precio_promedio',
                'precio_municipal','calidad')))
        }),
    )
    extra = 1

class MovimientoProductosProcesadosInline(admin.StackedInline):
    model = MovimientoProductosProcesados
    fieldsets = (
            (None, {
                'fields': ((('fkproducto_fresco'),
                ('volumen_venta_global','precio_promedio',
                'precio_municipal','calidad')))
        }),
    )
    extra = 1

class MovimientoAdmin(AutocompleteModelAdmin):
    search_fields = ['__unicode__']
    fieldsets = (
            (None, {
                'fields': (('nombre_mercado', 'fecha'),
                ('nombre_persona','organizacion_persona'),
                ('correo','telefono'))
        }),
    )
    related_search_fields = {

                'nombre_mercado': ('nombre_mercado',),
        }
    inlines = [MovimientoProductosFrescoInline, 
	           MovimientoProductosProcesadosInline]

admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(MovimientoProductosFresco)
admin.site.register(MovimientoProductosProcesados)