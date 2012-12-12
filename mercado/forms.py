from django.forms import ModelForm
from django import forms
from mercado.models import *


class ActividadForm(forms.ModelForm):
    
	class Meta:
		model = ActividadMercado
		widgets = {
				'apoyan_mercado' : forms.SelectMultiple(attrs={'class':'chosen'}),
				'productos_frescos' : forms.SelectMultiple(attrs={'class':'chosen'}),
				'productos_procesados' : forms.SelectMultiple(attrs={'class':'chosen'}),
		}	