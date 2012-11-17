# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Attack.guid'
        db.add_column('theapp_attack', 'guid',
                      self.gf('django.db.models.fields.CharField')(default='moo', max_length=300),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Attack.guid'
        db.delete_column('theapp_attack', 'guid')


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
            'guid': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raw_item': ('django.db.models.fields.TextField', [], {}),
            'when': ('django.db.models.fields.BigIntegerField', [], {})
        }
    }

    complete_apps = ['theapp']