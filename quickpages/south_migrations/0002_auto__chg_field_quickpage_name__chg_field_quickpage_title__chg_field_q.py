# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'QuickPage.name'
        db.alter_column('quickpages_quickpage', 'name', self.gf('django.db.models.fields.CharField')(max_length=513))

        # Changing field 'QuickPage.title'
        db.alter_column('quickpages_quickpage', 'title', self.gf('django.db.models.fields.CharField')(max_length=513))

        # Changing field 'QuickPage.javascript'
        db.alter_column('quickpages_quickpage', 'javascript', self.gf('django.db.models.fields.CharField')(max_length=1023))

        # Changing field 'QuickPage.slug'
        db.alter_column('quickpages_quickpage', 'slug', self.gf('django.db.models.fields.CharField')(unique=True, max_length=1023))

        # Changing field 'QuickPage.css'
        db.alter_column('quickpages_quickpage', 'css', self.gf('django.db.models.fields.CharField')(max_length=1023))


    def backwards(self, orm):
        
        # Changing field 'QuickPage.name'
        db.alter_column('quickpages_quickpage', 'name', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'QuickPage.title'
        db.alter_column('quickpages_quickpage', 'title', self.gf('django.db.models.fields.CharField')(max_length=512))

        # Changing field 'QuickPage.javascript'
        db.alter_column('quickpages_quickpage', 'javascript', self.gf('django.db.models.fields.CharField')(max_length=1024))

        # Changing field 'QuickPage.slug'
        db.alter_column('quickpages_quickpage', 'slug', self.gf('django.db.models.fields.CharField')(max_length=1024, unique=True))

        # Changing field 'QuickPage.css'
        db.alter_column('quickpages_quickpage', 'css', self.gf('django.db.models.fields.CharField')(max_length=1024))


    models = {
        'quickpages.quickpage': {
            'Meta': {'object_name': 'QuickPage'},
            'comments': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'css': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'heading': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'javascript': ('django.db.models.fields.CharField', [], {'max_length': '1023', 'blank': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '513'}),
            'published': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '1023'}),
            'template': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '513'}),
            'updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['quickpages']
