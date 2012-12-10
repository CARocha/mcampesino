# -*- coding: UTF-8 -*-
from django.db import models
from lugar.models import Comunidad, Departamento, Municipio, Pais
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Registro(models.Model):
	fecha_registro = models.DateField('Fecha de registro')
	nombre_persona = models.CharField('Nombre de persona que registra la informacion'
		                              , max_length=200)
	nombre_organizacion = models.CharField('Nombre de organización a que pertenece la persona'
		                              , max_length=200)
	correo = models.EmailField()
	telefono = models.IntegerField('Teléfono')

	class Meta:
		verbose_name=u'Registro de persona'

	def __unicode__(self):
		return u'%s || %s' % (self.nombre_persona, self.nombre_organizacion)

class RegistroMercado(models.Model):
	nombre_mercado = models.CharField('Nombre del mercado', 
		                               max_length=200)
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

	class Meta:
		verbose_name=u'Registro mercado'
		verbose_name_plural=u'Registro de mercados'

	def __unicode__(self):
		return self.nombre_mercado

class PersonaContacto(models.Model):
	nombre = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = 'Personas para contacto con mercados'

	def __unicode__(self):
		return self.nombre

class ActividadMercado(models.Model):
	fecha_actividad = models.DateField('Fecha de inicio de la actividad del mercado')
	direccion = models.TextField('Dirección física del mercado')
	persona_contacto = 	models.ForeignKey(PersonaContacto)
	telefono = models.IntegerField()    

