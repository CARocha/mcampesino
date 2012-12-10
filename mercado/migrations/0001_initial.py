# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registro'
        db.create_table('mercado_registro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_registro', self.gf('django.db.models.fields.DateField')()),
            ('nombre_persona', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_organizacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mercado', ['Registro'])

        # Adding model 'RegistroMercado'
        db.create_table('mercado_registromercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_mercado', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Pais'])),
            ('departamento', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
        ))
        db.send_create_signal('mercado', ['RegistroMercado'])

        # Adding model 'PersonaContacto'
        db.create_table('mercado_personacontacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['PersonaContacto'])

        # Adding model 'TipoOrganizacion'
        db.create_table('mercado_tipoorganizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['TipoOrganizacion'])

        # Adding model 'Periodicidad'
        db.create_table('mercado_periodicidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['Periodicidad'])

        # Adding model 'TiposOrganizacionesApoyan'
        db.create_table('mercado_tiposorganizacionesapoyan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['TiposOrganizacionesApoyan'])

        # Adding model 'ApoyanMercado'
        db.create_table('mercado_apoyanmercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo_organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.TiposOrganizacionesApoyan'])),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('mercado', ['ApoyanMercado'])

        # Adding model 'ProductosFrescos'
        db.create_table('mercado_productosfrescos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['ProductosFrescos'])

        # Adding model 'ProductosProcesados'
        db.create_table('mercado_productosprocesados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercado', ['ProductosProcesados'])

        # Adding model 'ActividadMercado'
        db.create_table('mercado_actividadmercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.RegistroMercado'])),
            ('fecha_actividad', self.gf('django.db.models.fields.DateField')()),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('persona_contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.PersonaContacto'])),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('pagina_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('tipo_organizacion_mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.TipoOrganizacion'])),
            ('modalidad', self.gf('django.db.models.fields.IntegerField')()),
            ('periodicidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.Periodicidad'])),
            ('vendedor_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('vendedor_mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('comprador_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('comprador_mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('abastecen_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('abastecen_mujer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mercado', ['ActividadMercado'])

        # Adding M2M table for field apoyan_mercado on 'ActividadMercado'
        db.create_table('mercado_actividadmercado_apoyan_mercado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercado.actividadmercado'], null=False)),
            ('apoyanmercado', models.ForeignKey(orm['mercado.apoyanmercado'], null=False))
        ))
        db.create_unique('mercado_actividadmercado_apoyan_mercado', ['actividadmercado_id', 'apoyanmercado_id'])

        # Adding M2M table for field productos_frescos on 'ActividadMercado'
        db.create_table('mercado_actividadmercado_productos_frescos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercado.actividadmercado'], null=False)),
            ('productosfrescos', models.ForeignKey(orm['mercado.productosfrescos'], null=False))
        ))
        db.create_unique('mercado_actividadmercado_productos_frescos', ['actividadmercado_id', 'productosfrescos_id'])

        # Adding M2M table for field productos_procesados on 'ActividadMercado'
        db.create_table('mercado_actividadmercado_productos_procesados', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercado.actividadmercado'], null=False)),
            ('productosprocesados', models.ForeignKey(orm['mercado.productosprocesados'], null=False))
        ))
        db.create_unique('mercado_actividadmercado_productos_procesados', ['actividadmercado_id', 'productosprocesados_id'])

        # Adding model 'Movimiento'
        db.create_table('mercado_movimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.RegistroMercado'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('nombre_persona', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('organizacion_persona', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mercado', ['Movimiento'])

        # Adding model 'MovimientoProductosFresco'
        db.create_table('mercado_movimientoproductosfresco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmovimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.Movimiento'])),
            ('producto_fresco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.ProductosFrescos'])),
            ('volumen_venta_global', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio', self.gf('django.db.models.fields.FloatField')()),
            ('precio_municipal', self.gf('django.db.models.fields.FloatField')()),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mercado', ['MovimientoProductosFresco'])

        # Adding model 'MovimientoProductosProcesados'
        db.create_table('mercado_movimientoproductosprocesados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmovimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.Movimiento'])),
            ('fkproducto_fresco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercado.ProductosFrescos'])),
            ('volumen_venta_global', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio', self.gf('django.db.models.fields.FloatField')()),
            ('precio_municipal', self.gf('django.db.models.fields.FloatField')()),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mercado', ['MovimientoProductosProcesados'])


    def backwards(self, orm):
        # Deleting model 'Registro'
        db.delete_table('mercado_registro')

        # Deleting model 'RegistroMercado'
        db.delete_table('mercado_registromercado')

        # Deleting model 'PersonaContacto'
        db.delete_table('mercado_personacontacto')

        # Deleting model 'TipoOrganizacion'
        db.delete_table('mercado_tipoorganizacion')

        # Deleting model 'Periodicidad'
        db.delete_table('mercado_periodicidad')

        # Deleting model 'TiposOrganizacionesApoyan'
        db.delete_table('mercado_tiposorganizacionesapoyan')

        # Deleting model 'ApoyanMercado'
        db.delete_table('mercado_apoyanmercado')

        # Deleting model 'ProductosFrescos'
        db.delete_table('mercado_productosfrescos')

        # Deleting model 'ProductosProcesados'
        db.delete_table('mercado_productosprocesados')

        # Deleting model 'ActividadMercado'
        db.delete_table('mercado_actividadmercado')

        # Removing M2M table for field apoyan_mercado on 'ActividadMercado'
        db.delete_table('mercado_actividadmercado_apoyan_mercado')

        # Removing M2M table for field productos_frescos on 'ActividadMercado'
        db.delete_table('mercado_actividadmercado_productos_frescos')

        # Removing M2M table for field productos_procesados on 'ActividadMercado'
        db.delete_table('mercado_actividadmercado_productos_procesados')

        # Deleting model 'Movimiento'
        db.delete_table('mercado_movimiento')

        # Deleting model 'MovimientoProductosFresco'
        db.delete_table('mercado_movimientoproductosfresco')

        # Deleting model 'MovimientoProductosProcesados'
        db.delete_table('mercado_movimientoproductosprocesados')


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
            'fkpais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
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
            'fkproducto_fresco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercado.ProductosFrescos']"}),
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
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.productosprocesados': {
            'Meta': {'object_name': 'ProductosProcesados'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercado.registro': {
            'Meta': {'object_name': 'Registro'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
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