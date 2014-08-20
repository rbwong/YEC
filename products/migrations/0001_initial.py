# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Product'
        db.create_table(u'products_product', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
            ('banner', self.gf('django.db.models.fields.files.ImageField')(default='banner-default.jpg', max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'products', ['Product'])


    def backwards(self, orm):
        # Deleting model 'Product'
        db.delete_table(u'products_product')


    models = {
        u'products.product': {
            'Meta': {'object_name': 'Product'},
            'banner': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'banner-default.jpg'", 'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['products']