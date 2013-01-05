# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from mercado.models import *
from mercado.forms import *


def index(request):
	mercados = RegistroMercado.objects.all()
	return render_to_response('index.html', {'mercados':mercados},
		                       context_instance=RequestContext(request))

def ver_mercado(request,id):
	mercado = get_object_or_404(RegistroMercado, id=id)
	productos_frescos = ProductosFrescos.objects.all()
	productos_procesados = ProductosProcesados.objects.all()

	return render_to_response('mercado.html', {'mercado':mercado, 
							  'productos_frescos':productos_frescos,
							  'productos_procesados':productos_procesados},
		                      context_instance=RequestContext(request))

def explorar(request):
	if request.method == 'POST':
		form = ActividadForm(request.POST)
		if form.is_valid():
			request.session['tipo_organizacion_mercado'] = form.cleaned_data['tipo_organizacion_mercado']            
			request.session['periodicidad'] = form.cleaned_data['periodicidad']
			request.session['productos_procesados'] = form.cleaned_data['productos_procesados']
			request.session['productos_frescos'] = form.cleaned_data['productos_frescos']
	else:
		form = ActividadForm()
	return render_to_response('explora.html', {'form':form},
		                      context_instance=RequestContext(request))