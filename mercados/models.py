# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Comunidad, Departamento, Municipio, Pais
from smart_selects.db_fields import ChainedForeignKey
from south.modelsinspector import add_introspection_rules
import os
from mcampesino.thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from productos.models import *

# Create your models here.
def get_file_path(intance,filename):
	return os.path.join(intance.fileDir, filename)


class Registro(models.Model):
	#fecha_registro = models.DateField('Fecha de  mercado')
	fecha_falguni = models.DateField(auto_now_add=True) #nose para que esta fecha :/
	nombre_persona = models.CharField('Nombre de persona que registra la informacion'
		                              , max_length=200)
	nombre_organizacion = models.CharField('Nombre de organización a que pertenece la persona'
		                              , max_length=200)
	correo = models.EmailField(null=True, blank=True)
	telefono = models.IntegerField('Teléfono',null=True, blank=True)

	class Meta:
		verbose_name=u'Registro de persona'

	def __unicode__(self):
		return u'%s || %s' % (self.nombre_persona, self.nombre_organizacion)

class RegistroMercado(models.Model):
	fkregistro = models.ForeignKey(Registro, verbose_name=u'Persona que registro')
	nombre_mercado = models.CharField('Nombre del mercado', 
		                               max_length=200)
	year = models.IntegerField('Año en que comenzo a funcionar el mercado')
	pais = models.ForeignKey(Pais)

	departamento = ChainedForeignKey(
		Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True
    )
	municipio = ChainedForeignKey(
        Municipio,
		chained_field="departamento",
		chained_model_field="departamento",
		show_all=False,
		auto_choose=True
    )
	comunidad = ChainedForeignKey(
		Comunidad,
		chained_field="municipio",
		chained_model_field="municipio",
		show_all=False,
		auto_choose=True
    )
	descripcion = models.TextField(null=True, blank=True)
	usuario = models.ForeignKey(User)

	class Meta:
		verbose_name=u'Registro mercado'
		verbose_name_plural=u'Registro de mercados'

	def foto(self):
		atach = Fotos.objects.filter(fk_mercado__id=self.id)
		return atach

	def __unicode__(self):
		return self.nombre_mercado

class Fotos(models.Model):
	nombre = models.CharField(max_length=150)
	picture = ImageWithThumbsField(upload_to=get_file_path,
		                           sizes=((460,260),(445,260),(200,200)),
		                           null=True, blank=True)

	fk_mercado = models.ForeignKey(RegistroMercado)
	fileDir = 'fotosmercados/'

	def __unicode__(self):
		return self.nombre

	class Meta:
		verbose_name_plural = "Fotos de los mercados"

class PersonaContacto(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Personas para contacto con mercados'

	def __unicode__(self):
		return self.nombre

class TipoOrganizacion(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Tipo de organización de los mercados'

	def __unicode__(self):
		return self.nombre

CHOICE_OPERACION = (
						(1, 'Mercado'),
						(2, 'Feria')
					)

class Periodicidad(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Periodicidad de operaciones'

	def __unicode__(self):
		return self.nombre

class TiposOrganizacionesApoyan(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Tipos de organizaciones'

	def __unicode__(self):
		return self.nombre

class ApoyanMercado(models.Model):
	nombre = models.CharField('Nombre de la organización', max_length=200)
	tipo_organizacion = models.ForeignKey(TiposOrganizacionesApoyan)
	correo = models.EmailField()

	class Meta:
		verbose_name_plural = 'Organizaciones apoyan mercados'

	def __unicode__(self):
		return self.nombre



class ActividadMercado(models.Model):
	fkmercado = models.ForeignKey(RegistroMercado, verbose_name=u'Mercados')
	fecha_actividad = models.DateField('Fecha actual del estado del mercado')
	direccion = models.TextField('Dirección física del mercado')
	persona_contacto = 	models.ForeignKey(PersonaContacto)
	telefono = models.IntegerField()    
	correo = models.EmailField()
	pagina_url = models.URLField('Página web', null=True, blank=True)
	tipo_organizacion_mercado = models.ForeignKey(TipoOrganizacion)
	modalidad = models.IntegerField('Modalidad de operación', 
		                            choices=CHOICE_OPERACION)
	periodicidad = models.ForeignKey(Periodicidad)
	vendedor_hombre = models.IntegerField()
	vendedor_mujer = models.IntegerField()
	comprador_hombre = models.IntegerField()
	comprador_mujer = models.IntegerField()
	abastecen_hombre = models.IntegerField()
	abastecen_mujer = models.IntegerField()
	apoyan_mercado = models.ManyToManyField(ApoyanMercado)
	productos_frescos = models.ManyToManyField(ProductosFrescos)
	productos_procesados = models.ManyToManyField(ProductosProcesados)

	class Meta:
		verbose_name_plural = "Estado actual del mercado"

	def __unicode__(self):
		return u'mercado: %s - %s' % (self.fkmercado, str(self.fecha_actividad)) 

