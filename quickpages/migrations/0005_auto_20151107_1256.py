# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('quickpages', '0004_auto_20151107_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickpage',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quicksnippet',
            name='css',
            field=models.TextField(help_text=b'CSS for this snippet - &lt;style&gt; tags will be passed through', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quicksnippet',
            name='js',
            field=models.TextField(help_text=b'Javascript for this snippet - &lt;script&gt; tags will be passed through', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quicksnippet',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
            preserve_default=True,
        ),
    ]
