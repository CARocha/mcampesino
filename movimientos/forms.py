# -*- coding: UTF-8 -*-

from django.forms import ModelForm
from django import forms
from mercados.models import *
from productos.models import *
from movimientos.models import *
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime

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


hoy = datetime.date.today()
class MovimientoForm(ModelForm):
	#nombre_mercado = forms.ModelChoiceField(widget=forms.Select, queryset=RegistroMercado.objects.all())
	
	# def __init__(self, user, *args, **kwargs):
	# 	super(MovimientoForm, self).__init__(*args, **kwargs)

	# 	if user.is_superuser:
	# 		self.fields['nombre_mercado'].queryset = RegistroMercado.objects.all()
	# 	else:
	# 		self.fields['nombre_mercado'].queryset = RegistroMercado.objects.filter(usuario=user)
	fecha = forms.DateField(label="Fecha de reporte", widget=SelectDateWidget(), initial=hoy)
	class Meta:
		model = Movimiento
		fields = ('nombre_mercado','fecha',)


class MovimientoProductosFrescoForm(forms.ModelForm):
	# lista_inicial = []
	# for producto in ProductosFrescos.objects.all():
	# 	lista_inicial.append({'producto':str(producto.nombre),})

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