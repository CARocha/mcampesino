# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Registro.fecha_falguni'
        db.add_column('mercado_registro', 'fecha_falguni',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 1, 9, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'ProductosProcesados.unidad'
        db.add_column('mercado_productosprocesados', 'unidad',
                      self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Registro.fecha_falguni'
        db.delete_column('mercado_registro', 'fecha_falguni')

        # Deleting field 'ProductosProcesados.unidad'
        db.delete_column('mercado_productosprocesados', 'unidad')


    models = {
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.pais': {
            'Meta': {'object_name': 'Pais'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.actividadmercado': {
            'Meta': {'object_name': 'ActividadMercado'},
            'abastecen_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'abastecen_mujer': ('django.db.models.fields.IntegerField', [], {}),
            'apoyan_mercado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mercado.ApoyanMercado']", 'symmetrical': 'False'}),
            'comprador_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'comprador_mujer': ('django.db.models.fields.IntegerField', [], {}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'fecha_actividad': ('django.db.models.fields.DateField', [], {}),
            'fkmercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.RegistroMercado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'periodicidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.Periodicidad']"}),
            'persona_contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.PersonaContacto']"}),
            'productos_frescos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mercado.ProductosFrescos']", 'symmetrical': 'False'}),
            'productos_procesados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mercado.ProductosProcesados']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_organizacion_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.TipoOrganizacion']"}),
            'vendedor_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'vendedor_mujer': ('django.db.models.fields.IntegerField', [], {})
        },
        'mercado.apoyanmercado': {
            'Meta': {'object_name': 'ApoyanMercado'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.TiposOrganizacionesApoyan']"})
        },
        'mercado.fotos': {
            'Meta': {'object_name': 'Fotos'},
            'fk_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.RegistroMercado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('mercado.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'mercado.movimiento': {
            'Meta': {'object_name': 'Movimiento'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.RegistroMercado']"}),
            'nombre_persona': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion_persona': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'mercado.movimientoproductosfresco': {
            'Meta': {'object_name': 'MovimientoProductosFresco'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'fkmovimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.Movimiento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_municipal': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio': ('django.db.models.fields.FloatField', [], {}),
            'producto_fresco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.ProductosFrescos']"}),
            'volumen_venta_global': ('django.db.models.fields.FloatField', [], {})
        },
        'mercado.movimientoproductosprocesados': {
            'Meta': {'object_name': 'MovimientoProductosProcesados'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'fkmovimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.Movimiento']"}),
            'fkproducto_fresco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.ProductosProcesados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_municipal': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio': ('django.db.models.fields.FloatField', [], {}),
            'volumen_venta_global': ('django.db.models.fields.FloatField', [], {})
        },
        'mercado.periodicidad': {
            'Meta': {'object_name': 'Periodicidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.personacontacto': {
            'Meta': {'object_name': 'PersonaContacto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.productosfrescos': {
            'Meta': {'object_name': 'ProductosFrescos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('mercado.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'mercado.productosprocesados': {
            'Meta': {'object_name': 'ProductosProcesados'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('mercado.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        'mercado.registro': {
            'Meta': {'object_name': 'Registro'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_falguni': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_organizacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_persona': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'mercado.registromercado': {
            'Meta': {'object_name': 'RegistroMercado'},
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fkregistro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.Registro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre_mercado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"})
        },
        'mercado.tipoorganizacion': {
            'Meta': {'object_name': 'TipoOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.tiposorganizacionesapoyan': {
            'Meta': {'object_name': 'TiposOrganizacionesApoyan'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mercado']