# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProductosFrescos'
        db.create_table('productos_productosfrescos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('picture', self.gf('mcampesino.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('productos', ['ProductosFrescos'])

        # Adding model 'ProductosProcesados'
        db.create_table('productos_productosprocesados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('unidad', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('picture', self.gf('mcampesino.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal('productos', ['ProductosProcesados'])

    def backwards(self, orm):
        # Deleting model 'ProductosFrescos'
        db.delete_table('productos_productosfrescos')

        # Deleting model 'ProductosProcesados'
        db.delete_table('productos_productosprocesados')

    models = {
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

    complete_apps = ['productos']