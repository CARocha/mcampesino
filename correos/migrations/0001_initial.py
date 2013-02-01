# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Correos'
        db.create_table('correos_correos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('persona', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('correos', ['Correos'])


    def backwards(self, orm):
        # Deleting model 'Correos'
        db.delete_table('correos_correos')


    models = {
        'correos.correos': {
            'Meta': {'object_name': 'Correos'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'persona': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['correos']