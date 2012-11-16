# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Area.center_long'
        db.alter_column('theapp_area', 'center_long', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Area.english_name'
        db.alter_column('theapp_area', 'english_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True))

        # Changing field 'Area.center_lat'
        db.alter_column('theapp_area', 'center_lat', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'Attack.area'
        db.alter_column('theapp_attack', 'area_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['theapp.Area'], null=True))

    def backwards(self, orm):

        # Changing field 'Area.center_long'
        db.alter_column('theapp_area', 'center_long', self.gf('django.db.models.fields.FloatField')(default=''))

        # Changing field 'Area.english_name'
        db.alter_column('theapp_area', 'english_name', self.gf('django.db.models.fields.CharField')(default='', max_length=200))

        # Changing field 'Area.center_lat'
        db.alter_column('theapp_area', 'center_lat', self.gf('django.db.models.fields.FloatField')(default=''))

        # Changing field 'Attack.area'
        db.alter_column('theapp_attack', 'area_id', self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['theapp.Area']))

    models = {
        'theapp.area': {
            'Meta': {'object_name': 'Area'},
            'center_lat': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'center_long': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'english_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True'}),
            'hebrew_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'theapp.attack': {
            'Meta': {'object_name': 'Attack'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['theapp.Area']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_item': ('django.db.models.fields.TextField', [], {}),
            'when': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['theapp']