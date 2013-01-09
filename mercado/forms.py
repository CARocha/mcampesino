from django.forms import ModelForm
from django import forms
from mercado.models import *
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory


class ActividadForm(forms.Form):
	tipo_organizacion_mercado = forms.ModelChoiceField(queryset=TipoOrganizacion.objects.all(),
    	                                               required=False, label="Organizacion")
	periodicidad = forms.ModelChoiceField(queryset=Periodicidad.objects.all(),
    									  required=False, label="periodicidad")
	productos_procesados = forms.ModelChoiceField(queryset=ProductosProcesados.objects.all(),
    											  required=False, label="produc. procesados")
	productos_frescos = forms.ModelChoiceField(queryset=ProductosFrescos.objects.all(),
    										   required=False, label="produc. frescos")
	class Meta:
		model = ActividadMercado
		#fields = ('tipo_organizacion_mercado','periodicidad','productos_procesados','productos_frescos')


class MovimientoForm(forms.ModelForm):
	#mercado = forms.ModelChoiceField(widget=forms.Select, queryset=RegistroMercado.objects.all())
	class Meta:
		model = Movimiento
		exclude = ('usuario',)


class MovimientoProductosFrescoForm(forms.ModelForm):
	lista_inicial = []
	for producto in ProductosFrescos.objects.all():
		lista_inicial.append({'producto':str(producto.nombre),})

	# def __init__(self, *args, **kwargs):
	# 	if not kwargs['initial']:
	# 		kwargs['initial'] = {}
	# 	kwargs['initial'].update({'nombre':'caramelo'})
	# 	super(MovimientoProductosFrescoForm, self).__init__(*args, **kwargs)
	# 	self.initial = [{'nombre':'caramelo'},{'nombre':'nose'},]

	class Meta:
		model = MovimientoProductosFresco
		exclude = ('fkmovimiento',)

# FrescoFormSet = modelformset_factory(ProductosFrescos, formset=BaseFrescoFormSet)
# formset_fresco = FrescoFormSet(queryset=ProductosFrescos.objects.none())
# class MovimientoProductosProcesadoForm(forms.ModelForm):
# 	class Meta:
# 		model = MovimientoProductosProcesado
# 		exclude = ('fkmovimiento',)