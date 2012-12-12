from django.forms import ModelForm
from django import forms
from models import *


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('apoyan_mercado',)
        widgets = {
            		'apoyan_mercado': SelectMultiple(attrs={'class': 'chosen'}),
            	  }

    