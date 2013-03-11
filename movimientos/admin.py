# -*- coding: UTF-8 -*-
from django.contrib import admin
from autocomplete.widgets import *
from mercados.models import *
from productos.models import *
from movimientos.forms import *
from django.forms.models import BaseInlineFormSet


class RegistroMercadoInline(admin.StackedInline):
	model = RegistroMercado
	extra = 1

class FotosInline(admin.StackedInline):
    model = Fotos
    extra = 1

class RegistroAdmin(admin.ModelAdmin):
	inlines = [RegistroMercadoInline]

class RegistroMercadoAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.usuario = request.user
        obj.save()
        
    def queryset(self, request):
        qs = super(RegistroMercadoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)
    exclude = ('usuario',)
    inlines = [FotosInline]

admin.site.register(Registro)
admin.site.register(RegistroMercado, RegistroMercadoAdmin)
admin.site.register(PersonaContacto)
admin.site.register(TipoOrganizacion)
admin.site.register(Periodicidad)
admin.site.register(TiposOrganizacionesApoyan)
admin.site.register(ApoyanMercado)
admin.site.register(ProductosFrescos)
admin.site.register(ProductosProcesados)
admin.site.register(Fotos)

class ActividadMercadoAdmin(admin.ModelAdmin):

    def queryset(self, request):
        qs = super(ActividadMercadoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(fkmercado__usuario=request.user)

	filter_horizontal = ('apoyan_mercado','productos_frescos','productos_procesados')
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


class MovimientoProductosFrescoInline(admin.TabularInline):
    model = MovimientoProductosFresco

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     for producto in ProductosFrescos.objects.all():
    #         if db_field.name == 'producto_fresco':
    #             kwargs['initial'] = [{'producto_fresco': producto.nombre}] #request.GET.get('producto_fresco', '')
    #         return super(MovimientoProductosFrescoInline, self).formfield_for_foreignkey(db_field, request, **kwargs)

    fieldsets = (
            (None, {
                'fields': (('producto_fresco',
                'volumen_venta_global','precio_promedio',
                'precio_municipal','calidad'),)
        }),
    )
    extra = 0
    max_num = 0
    

class MovimientoProductosProcesadosInline(admin.TabularInline):
    model = MovimientoProductosProcesados
    fieldsets = (
            (None, {
                'fields': (('fkproducto_fresco',
                'volumen_venta_global','precio_promedio',
                'precio_municipal','calidad'),)
        }),
    )
    extra = 0
    max_num = 0

class MovimientoAdmin(AutocompleteModelAdmin):

    def queryset(self, request):
        qs = super(MovimientoAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(usuario=request.user)

    search_fields = ['__unicode__']
    list_display = ['__unicode__', 'fecha']
    list_filter = ['nombre_mercado']
    date_hierarchy = 'fecha'
    related_search_fields = {

                'nombre_mercado': ('nombre_mercado',),
        }
    inlines = [MovimientoProductosFrescoInline, 
	           MovimientoProductosProcesadosInline]

admin.site.register(Movimiento, MovimientoAdmin)
admin.site.register(MovimientoProductosFresco)
admin.site.register(MovimientoProductosProcesados)