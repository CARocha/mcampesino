
# -*- coding: UTF-8 -*-
from django.db import models
import os
from mcampesino.thumbs import ImageWithThumbsField


# Create your models here.

def get_file_path(intance,filename):
	return os.path.join(intance.fileDir, filename)

class ProductosFrescos(models.Model):
	nombre = models.CharField(max_length=200)
	unidad = models.CharField(max_length=15, null=True, blank=True)
	picture = ImageWithThumbsField(upload_to=get_file_path,
		                            sizes=((60,60),(200,200)),
		                            null=True, blank=True)

	fileDir = 'fresco/'

	class Meta:
		verbose_name_plural = 'Productos frescos'

	def __unicode__(self):
		return self.nombre

	def fresco_unidad(self):
		return u'%s || %s' % (self.nombre,self.unidad)

class ProductosProcesados(models.Model):
	nombre = models.CharField(max_length=200)
	unidad = models.CharField(max_length=15, null=True, blank=True)
	picture = ImageWithThumbsField(upload_to=get_file_path,
		                           sizes=((60,60),(200,200)),
		                           null=True, blank=True)

	fileDir = 'procesados/'

	class Meta:
		verbose_name_plural = 'Productos procesados'

	def __unicode__(self):
		return self.nombre

	def procesado_unidad(self):
		return u'%s || %s' % (self.nombre,self.unidad)