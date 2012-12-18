from django.forms import ModelForm
from django import forms
from mercado.models import *


class ActividadForm(forms.ModelForm):
    
	class Meta:
		model = ActividadMercado

#MovimiendotFormset = forms.models.inlineformset_factory(MovimientoProductosFresco,MovimientoProductosProcesados)
class MovimientoProductosFrescoForm(forms.ModelForm):
	# def __init__(self, **kwargs):
	# 	super(MovimientoProductosFrescoForm, self).__init__(**kwargs)
	# 	self.movimiento_forset = MovimiendotFormset(instance=self.instance, data=self.data,
	# 		prefix=self.prefix)

	# def is_valid(self):
	# 	return (super(MovimientoProductosFrescoForm, self).is_valid() and 
	# 			self.movimiento_forset.is_valid())

	# def save(self, commit=True):
	# 	assert commit == True 
	# 	res = super(MovimientoProductosFrescoForm, self).save(commit=commit)
	# 	self.movimiento_forset.save()
	# 	return res

	class Meta:
		model = MovimientoProductosFresco
		exclude = ('fkmovimiento',)

# class MovimientoProductosProcesadoForm(forms.ModelForm):
# 	class Meta:
# 		model = MovimientoProductosProcesado
# 		exclude = ('fkmovimiento',)