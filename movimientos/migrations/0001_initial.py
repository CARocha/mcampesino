# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movimiento'
        db.create_table('movimientos_movimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.RegistroMercado'])),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('organizacion_persona', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('movimientos', ['Movimiento'])

        # Adding model 'MovimientoProductosFresco'
        db.create_table('movimientos_movimientoproductosfresco', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmovimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movimientos.Movimiento'])),
            ('producto_fresco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.ProductosFrescos'])),
            ('volumen_venta_global', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio', self.gf('django.db.models.fields.FloatField')()),
            ('precio_municipal', self.gf('django.db.models.fields.FloatField')()),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('movimientos', ['MovimientoProductosFresco'])

        # Adding model 'MovimientoProductosProcesados'
        db.create_table('movimientos_movimientoproductosprocesados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmovimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['movimientos.Movimiento'])),
            ('fkproducto_fresco', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['productos.ProductosProcesados'])),
            ('volumen_venta_global', self.gf('django.db.models.fields.FloatField')()),
            ('precio_promedio', self.gf('django.db.models.fields.FloatField')()),
            ('precio_municipal', self.gf('django.db.models.fields.FloatField')()),
            ('calidad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('movimientos', ['MovimientoProductosProcesados'])

    def backwards(self, orm):
        # Deleting model 'Movimiento'
        db.delete_table('movimientos_movimiento')

        # Deleting model 'MovimientoProductosFresco'
        db.delete_table('movimientos_movimientoproductosfresco')

        # Deleting model 'MovimientoProductosProcesados'
        db.delete_table('movimientos_movimientoproductosprocesados')

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'mercados.registro': {
            'Meta': {'object_name': 'Registro'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha_falguni': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_organizacion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_persona': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'mercados.registromercado': {
            'Meta': {'object_name': 'RegistroMercado'},
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'departamento': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'descripcion': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'fkregistro': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.Registro']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre_mercado': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Pais']"}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'movimientos.movimiento': {
            'Meta': {'object_name': 'Movimiento'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.RegistroMercado']"}),
            'organizacion_persona': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'movimientos.movimientoproductosfresco': {
            'Meta': {'object_name': 'MovimientoProductosFresco'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'fkmovimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movimientos.Movimiento']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_municipal': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio': ('django.db.models.fields.FloatField', [], {}),
            'producto_fresco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['productos.ProductosFrescos']"}),
            'volumen_venta_global': ('django.db.models.fields.FloatField', [], {})
        },
        'movimientos.movimientoproductosprocesados': {
            'Meta': {'object_name': 'MovimientoProductosProcesados'},
            'calidad': ('django.db.models.fields.IntegerField', [], {}),
            'fkmovimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['movimientos.Movimiento']"}),
            'fkproducto_fresco': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['productos.ProductosProcesados']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'precio_municipal': ('django.db.models.fields.FloatField', [], {}),
            'precio_promedio': ('django.db.models.fields.FloatField', [], {}),
            'volumen_venta_global': ('django.db.models.fields.FloatField', [], {})
        },
        'productos.productosfrescos': {
            'Meta': {'object_name': 'ProductosFrescos'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('mcampesino.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        },
        'productos.productosprocesados': {
            'Meta': {'object_name': 'ProductosProcesados'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'picture': ('mcampesino.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'unidad': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['movimientos']