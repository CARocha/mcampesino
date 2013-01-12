# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Registro'
        db.create_table('mercados_registro', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_registro', self.gf('django.db.models.fields.DateField')()),
            ('fecha_falguni', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
            ('nombre_persona', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_organizacion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('telefono', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('mercados', ['Registro'])

        # Adding model 'RegistroMercado'
        db.create_table('mercados_registromercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkregistro', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.Registro'])),
            ('nombre_mercado', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Pais'])),
            ('departamento', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('descripcion', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('usuario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('mercados', ['RegistroMercado'])

        # Adding model 'Fotos'
        db.create_table('mercados_fotos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('picture', self.gf('mcampesino.thumbs.ImageWithThumbsField')(max_length=100, null=True, blank=True)),
            ('fk_mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.RegistroMercado'])),
        ))
        db.send_create_signal('mercados', ['Fotos'])

        # Adding model 'PersonaContacto'
        db.create_table('mercados_personacontacto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercados', ['PersonaContacto'])

        # Adding model 'TipoOrganizacion'
        db.create_table('mercados_tipoorganizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercados', ['TipoOrganizacion'])

        # Adding model 'Periodicidad'
        db.create_table('mercados_periodicidad', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercados', ['Periodicidad'])

        # Adding model 'TiposOrganizacionesApoyan'
        db.create_table('mercados_tiposorganizacionesapoyan', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('mercados', ['TiposOrganizacionesApoyan'])

        # Adding model 'ApoyanMercado'
        db.create_table('mercados_apoyanmercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tipo_organizacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.TiposOrganizacionesApoyan'])),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal('mercados', ['ApoyanMercado'])

        # Adding model 'ActividadMercado'
        db.create_table('mercados_actividadmercado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkmercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.RegistroMercado'])),
            ('fecha_actividad', self.gf('django.db.models.fields.DateField')()),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('persona_contacto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.PersonaContacto'])),
            ('telefono', self.gf('django.db.models.fields.IntegerField')()),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('pagina_url', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('tipo_organizacion_mercado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.TipoOrganizacion'])),
            ('modalidad', self.gf('django.db.models.fields.IntegerField')()),
            ('periodicidad', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mercados.Periodicidad'])),
            ('vendedor_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('vendedor_mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('comprador_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('comprador_mujer', self.gf('django.db.models.fields.IntegerField')()),
            ('abastecen_hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('abastecen_mujer', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('mercados', ['ActividadMercado'])

        # Adding M2M table for field apoyan_mercado on 'ActividadMercado'
        db.create_table('mercados_actividadmercado_apoyan_mercado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercados.actividadmercado'], null=False)),
            ('apoyanmercado', models.ForeignKey(orm['mercados.apoyanmercado'], null=False))
        ))
        db.create_unique('mercados_actividadmercado_apoyan_mercado', ['actividadmercado_id', 'apoyanmercado_id'])

        # Adding M2M table for field productos_frescos on 'ActividadMercado'
        db.create_table('mercados_actividadmercado_productos_frescos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercados.actividadmercado'], null=False)),
            ('productosfrescos', models.ForeignKey(orm['productos.productosfrescos'], null=False))
        ))
        db.create_unique('mercados_actividadmercado_productos_frescos', ['actividadmercado_id', 'productosfrescos_id'])

        # Adding M2M table for field productos_procesados on 'ActividadMercado'
        db.create_table('mercados_actividadmercado_productos_procesados', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('actividadmercado', models.ForeignKey(orm['mercados.actividadmercado'], null=False)),
            ('productosprocesados', models.ForeignKey(orm['productos.productosprocesados'], null=False))
        ))
        db.create_unique('mercados_actividadmercado_productos_procesados', ['actividadmercado_id', 'productosprocesados_id'])

    def backwards(self, orm):
        # Deleting model 'Registro'
        db.delete_table('mercados_registro')

        # Deleting model 'RegistroMercado'
        db.delete_table('mercados_registromercado')

        # Deleting model 'Fotos'
        db.delete_table('mercados_fotos')

        # Deleting model 'PersonaContacto'
        db.delete_table('mercados_personacontacto')

        # Deleting model 'TipoOrganizacion'
        db.delete_table('mercados_tipoorganizacion')

        # Deleting model 'Periodicidad'
        db.delete_table('mercados_periodicidad')

        # Deleting model 'TiposOrganizacionesApoyan'
        db.delete_table('mercados_tiposorganizacionesapoyan')

        # Deleting model 'ApoyanMercado'
        db.delete_table('mercados_apoyanmercado')

        # Deleting model 'ActividadMercado'
        db.delete_table('mercados_actividadmercado')

        # Removing M2M table for field apoyan_mercado on 'ActividadMercado'
        db.delete_table('mercados_actividadmercado_apoyan_mercado')

        # Removing M2M table for field productos_frescos on 'ActividadMercado'
        db.delete_table('mercados_actividadmercado_productos_frescos')

        # Removing M2M table for field productos_procesados on 'ActividadMercado'
        db.delete_table('mercados_actividadmercado_productos_procesados')

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
        'mercados.actividadmercado': {
            'Meta': {'object_name': 'ActividadMercado'},
            'abastecen_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'abastecen_mujer': ('django.db.models.fields.IntegerField', [], {}),
            'apoyan_mercado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mercados.ApoyanMercado']", 'symmetrical': 'False'}),
            'comprador_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'comprador_mujer': ('django.db.models.fields.IntegerField', [], {}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'fecha_actividad': ('django.db.models.fields.DateField', [], {}),
            'fkmercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.RegistroMercado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {}),
            'pagina_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'periodicidad': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.Periodicidad']"}),
            'persona_contacto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.PersonaContacto']"}),
            'productos_frescos': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['productos.ProductosFrescos']", 'symmetrical': 'False'}),
            'productos_procesados': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['productos.ProductosProcesados']", 'symmetrical': 'False'}),
            'telefono': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_organizacion_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.TipoOrganizacion']"}),
            'vendedor_hombre': ('django.db.models.fields.IntegerField', [], {}),
            'vendedor_mujer': ('django.db.models.fields.IntegerField', [], {})
        },
        'mercados.apoyanmercado': {
            'Meta': {'object_name': 'ApoyanMercado'},
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tipo_organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.TiposOrganizacionesApoyan']"})
        },
        'mercados.fotos': {
            'Meta': {'object_name': 'Fotos'},
            'fk_mercado': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mercados.RegistroMercado']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'picture': ('mcampesino.thumbs.ImageWithThumbsField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'mercados.periodicidad': {
            'Meta': {'object_name': 'Periodicidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercados.personacontacto': {
            'Meta': {'object_name': 'PersonaContacto'},
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
        'mercados.tipoorganizacion': {
            'Meta': {'object_name': 'TipoOrganizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'mercados.tiposorganizacionesapoyan': {
            'Meta': {'object_name': 'TiposOrganizacionesApoyan'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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

    complete_apps = ['mercados']