from django.forms import ModelForm
from django import forms
from mercado.models import *
from django.forms.formsets import formset_factory
from django.forms.models import inlineformset_factory
from django.forms.models import BaseModelFormSet
from django.forms.models import modelformset_factory


class BaseFrescoFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        self.queryset = ProductosFrescos.objects.all()
        super(BaseFrescoFormSet, self).__init__(*args, **kwargs)

class ActividadForm(forms.ModelForm):
    
	class Meta:
		model = ActividadMercado

class MovimientoProductosFrescoForm(forms.ModelForm):

	class Meta:
		model = MovimientoProductosFresco
		exclude = ('fkmovimiento',)

FrescoFormSet = modelformset_factory(ProductosFrescos, formset=BaseFrescoFormSet)
formset_fresco = FrescoFormSet(queryset=ProductosFrescos.objects.none())
# class MovimientoProductosProcesadoForm(forms.ModelForm):
# 	class Meta:
# 		model = MovimientoProductosProcesado
# 		exclude = ('fkmovimiento',)