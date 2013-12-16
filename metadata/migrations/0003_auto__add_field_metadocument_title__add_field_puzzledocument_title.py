# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'MetaDocument.title'
        db.add_column(u'metadata_metadocument', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Hello', max_length='128'),
                      keep_default=False)

        # Adding field 'PuzzleDocument.title'
        db.add_column(u'metadata_puzzledocument', 'title',
                      self.gf('django.db.models.fields.CharField')(default='Hello', max_length='128'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'MetaDocument.title'
        db.delete_column(u'metadata_metadocument', 'title')

        # Deleting field 'PuzzleDocument.title'
        db.delete_column(u'metadata_puzzledocument', 'title')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'metadata.meta': {
            'Meta': {'object_name': 'Meta'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'metas'", 'to': u"orm['metadata.PuzzleTeam']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        },
        u'metadata.metadocument': {
            'Meta': {'object_name': 'MetaDocument'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['metadata.Meta']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        },
        u'metadata.puzzle': {
            'Meta': {'object_name': 'Puzzle'},
            'answer': ('django.db.models.fields.CharField', [], {'max_length': "'128'"}),
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'puzzles'", 'to': u"orm['metadata.Meta']"}),
            'solved': ('django.db.models.fields.BooleanField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        },
        u'metadata.puzzledocument': {
            'Meta': {'object_name': 'PuzzleDocument'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'link_type': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            'puzzle': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'documents'", 'to': u"orm['metadata.Puzzle']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        },
        u'metadata.puzzleteam': {
            'Meta': {'object_name': 'PuzzleTeam'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': "'128'"})
        },
        u'metadata.puzzleteammembership': {
            'Meta': {'object_name': 'PuzzleTeamMembership'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'team': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['metadata.PuzzleTeam']"})
        }
    }

    complete_apps = ['metadata']