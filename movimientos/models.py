# -*- coding: UTF-8 -*-
from django.db import models
import os
from django.contrib.auth.models import User
from productos.models import *
from mercados.models import *
import datetime



#add_introspection_rules([], ["^thumbs\.ImageWithThumbsField"])

# Create your models here.
def get_file_path(intance,filename):
	return os.path.join(intance.fileDir, filename)



#------------------ Movimiento de los productos en el mercado campesino

class Movimiento(models.Model):
	nombre_mercado = models.ForeignKey(RegistroMercado)
	fecha = models.DateField('Fecha de reporte')
	usuario = models.ForeignKey(User)

	class Meta:
		verbose_name_plural = "Movimiento de los productos en el mercado"

	def __unicode__(self):
		return self.nombre_mercado.nombre_mercado

CHOICE_CALIDAD = (
					(1, 'Excelente'),
					(2, 'Muy buena'),
					(3, 'Buena'),
					(4, 'Mala')
	             )

class MovimientoProductosFresco(models.Model):
	fkmovimiento = models.ForeignKey(Movimiento)
	producto_fresco = models.ForeignKey(ProductosFrescos)
	volumen_venta_global = models.FloatField()
	precio_promedio = models.FloatField()
	precio_municipal = models.FloatField()
	calidad = models.IntegerField(choices=CHOICE_CALIDAD)

	class Meta:
		verbose_name_plural = "Movimiento de productos frescos"


class MovimientoProductosProcesados(models.Model):
	fkmovimiento = models.ForeignKey(Movimiento)
	fkproducto_fresco = models.ForeignKey(ProductosProcesados, verbose_name=u'Producto procesados')
	volumen_venta_global = models.FloatField()
	precio_promedio = models.FloatField()
	precio_municipal = models.FloatField()
	calidad = models.IntegerField(choices=CHOICE_CALIDAD)

	class Meta:
		verbose_name_plural = "Movimiento de productos procesados"
