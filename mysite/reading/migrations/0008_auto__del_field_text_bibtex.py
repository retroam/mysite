# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Text.bibtex'
        db.delete_column('reading_text', 'bibtex')


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Text.bibtex'
        raise RuntimeError("Cannot reverse this migration. 'Text.bibtex' and its values cannot be restored.")


    models = {
        'reading.note': {
            'Meta': {'object_name': 'Note'},
            'created': ('django.db.models.fields.DateTimeField', [], {'unique': 'True', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'markdown': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'text': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notes'", 'to': "orm['reading.Text']"})
        },
        'reading.text': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Text'},
            'citation_key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'db_index': 'True'}),
            'citation_text': ('django.db.models.fields.CharField', [], {'max_length': '128', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'markdown': ('django.db.models.fields.TextField', [], {}),
            'modified': ('django.db.models.fields.DateTimeField', [], {}),
            'related_texts': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'related_texts_rel_+'", 'to': "orm['reading.Text']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '80', 'db_index': 'True'}),
            'small_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '16'}),
            'synopsis': ('django.db.models.fields.TextField', [], {}),
            'zotero_id': ('django.db.models.fields.CharField', [], {'max_length': '16', 'blank': 'True'}),
            'zotero_json': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['reading']
