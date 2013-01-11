# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from mercado.models import *
from mercado.forms import *
from django.utils import simplejson as json
from django.core import serializers

def reqdata(request):
	mensaje = ''
	if request.is_ajax() and request.method == 'POST':
		productosfrescos = ProductosFrescos.objects.filter(actividadmercado__fkmercado__id=request.POST['mercado'])
		productosprocedados = ProductosProcesados.objects.filter(actividadmercado__fkmercado__id=request.POST['mercado'])
		prod1 = {x.id:x.nombre for x in productosfrescos}
		prod2 = {x.id:x.nombre for x in productosprocedados}
		uni1 = {x.id:x.unidad for x in productosfrescos}
		uni2 = {x.id:x.unidad for x in productosprocedados}
		#dati = serializers.serialize('json', ProductosFrescos.objects.filter(actividadmercado__fkmercado__id=request.POST['mercado']).values('id','nombre','unidad'))
		#pf = ProductosFrescos.objects.filter(actividadmercado__fkmercado__id=request.POST['mercado']).values_list('id','nombre', 'unidad') 
		mensaje = json.dumps(dict(productos=prod1,procesado=prod2,unidadf=uni1,unidadp=uni2))
	return HttpResponse(mensaje)

def multipleform(request):
	# lista_inicial = []
	# for producto in ProductosFrescos.objects.all():
	# 	lista_inicial.append({'producto_fresco':producto.id,'volumen_venta_global':0.0,
	# 		                   'precio_promedio':0.0,'precio_municipal':0.0})
	# FrescoFormSet = formset_factory(MovimientoProductosFrescoForm, 
	# 	                            extra=len(lista_inicial), 
	# 	                            max_num=len(lista_inicial))
	# formset = FrescoFormSet(initial=lista_inicial)
	# if request.method == 'POST':
	# 	form = formset(request.POST)
	# 	form1 = MovimientoForm(request.POST)
	# 	if formset.is_valid() and form1.is_valid():
	# 		form1.save()
	# 		form.save()	
	# else:
	# 	formset = FrescoFormSet(initial=lista_inicial)
	# 	form1 = MovimientoForm()
	if request.method == 'POST':
		formMer = MovimientoForm(request.POST)


		if formMer.is_valid():
			form_uncommited = formMer.save(commit=False)
			form_uncommited.usuario = request.user
			form_uncommited.save()
			for prod in ProductosFrescos.objects.all():
				producto = request.POST.get('product-'+str(prod.id), None)
				volumen = request.POST.get('volumen-'+str(prod.id), None)
				promedio = request.POST.get('promedio-'+str(prod.id), None)
				municipal = request.POST.get('municipal-'+str(prod.id), None)
				calidad = request.POST.get('calidad-'+str(prod.id), None)
				if producto and volumen and promedio and municipal and calidad: 
					mov = MovimientoProductosFresco.objects.create(
	                    fkmovimiento=form_uncommited,
	                    producto_fresco = ProductosFrescos.objects.get(pk=prod.id),
	                    volumen_venta_global = volumen,
	                    precio_promedio = promedio,
	                    precio_municipal = municipal,
	                    calidad = calidad
	                )
					mov.save()
			for prod in ProductosProcesados.objects.all():
				productop = request.POST.get('productp-'+str(prod.id), None)
				volumenp = request.POST.get('volumenp-'+str(prod.id), None)
				promediop = request.POST.get('promediop-'+str(prod.id), None)
				municipalp = request.POST.get('municipalp-'+str(prod.id), None)
				calidadp = request.POST.get('calidadp-'+str(prod.id), None)
				if productop and volumenp and promediop and municipalp and calidadp: 
					movp = MovimientoProductosProcesados.objects.create(
	                    fkmovimiento=form_uncommited,
	                    fkproducto_fresco = ProductosProcesados.objects.get(pk=prod.id),
	                    volumen_venta_global = volumenp,
	                    precio_promedio = promediop,
	                    precio_municipal = municipalp,
	                    calidad = calidadp
	                )
					movp.save()
	else:
		formMer = MovimientoForm()
	
		
	return render_to_response('test.html', {'formMer':formMer},
							  context_instance=RequestContext(request))


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