# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table('theapp_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hebrew_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('english_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('center_long', self.gf('django.db.models.fields.FloatField')()),
            ('center_lat', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('theapp', ['Area'])

        # Adding model 'Attack'
        db.create_table('theapp_attack', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theapp.Area'])),
            ('when', self.gf('django.db.models.fields.BigIntegerField')()),
            ('raw_item', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('theapp', ['Attack'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table('theapp_area')

        # Deleting model 'Attack'
        db.delete_table('theapp_attack')


    models = {
        'theapp.area': {
            'Meta': {'object_name': 'Area'},
            'center_lat': ('django.db.models.fields.FloatField', [], {}),
            'center_long': ('django.db.models.fields.FloatField', [], {}),
            'english_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hebrew_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'theapp.attack': {
            'Meta': {'object_name': 'Attack'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['theapp.Area']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_item': ('django.db.models.fields.TextField', [], {}),
            'when': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['theapp']