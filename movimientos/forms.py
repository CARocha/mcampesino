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
    	                                               required=False, label="Organizacion",empty_label="Organización")
	periodicidad = forms.ModelChoiceField(queryset=Periodicidad.objects.all(),
    									  required=False, label="periodicidad", empty_label="Periodicidad")
	productos_procesados = forms.ModelChoiceField(queryset=ProductosProcesados.objects.all(),
    											  required=False, label="produc. procesados", empty_label="Prod. Procesados")
	productos_frescos = forms.ModelChoiceField(queryset=ProductosFrescos.objects.all(),
    										   required=False, label="produc. frescos" , empty_label="Prod. Frescos")
	class Meta:
		model = ActividadMercado

YEAR_CHOICES = ('2011', '2012', '2013','2014', '2015', '2016','2017', '2018', '2019')
hoy = datetime.date.today()
class MovimientoForm(ModelForm):
	fecha = forms.DateField(label="Fecha de reporte", widget=SelectDateWidget(years=YEAR_CHOICES), initial=hoy)
	class Meta:
		model = Movimiento
		fields = ('nombre_mercado','fecha',)


class MovimientoProductosFrescoForm(forms.ModelForm):

	class Meta:
		model = MovimientoProductosFresco
		exclude = ('fkmovimiento',)