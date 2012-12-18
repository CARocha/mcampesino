from django.forms import ModelForm
from django import forms
from mercado.models import *


class ActividadForm(forms.ModelForm):
    
	class Meta:
		model = ActividadMercado