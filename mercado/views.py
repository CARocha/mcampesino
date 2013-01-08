# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse
from mercado.models import *
from mercado.forms import *
from django.utils import simplejson as json

def reqdata(request):
    mensaje = ''
    if request.is_ajax() and request.method == 'POST':
        productosfrescos = ProductosFrescos.objects.filter(actividadmercado__fkmercado__id=request.POST['mercado'])
        #productosprocedados = ProductosProcesados.objects.filter(actividadmercado__fkmercado__nombre_mercado=request.POST['mercado'])
        prod1 = {x.id:x.nombre for x in productosfrescos}
        #prod2 = {x.id:x.nombre for x in productosprocedados}
        mensaje = json.dumps(dict(productos=prod1))
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
		for prod in ProductosFrescos.objects.all():
			producto = request.POST.get('product-'+str(prod.id), None)
			cantidad = request.POST.get('cant-'+str(prod.id), None)
			if producto and cantidad:
				mov = MovimientoProducto.objects.create(
                    mercado=Mercado.objects.get(pk=request.POST['mercado']),
                    producto = Producto.objects.get(pk=prod.id),
                    cantidad = cantidad
                )
				mov.save()

	formMer = MercadoForm()
		
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