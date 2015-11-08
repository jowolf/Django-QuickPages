# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0003_auto_20150923_1649'),
    ]

    operations = [
        #migrations.DeleteModel(
        #    name='QuickSnippet',
        #),
        migrations.CreateModel(
            name='QuickSnippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Name, identifier-style, no spaces, will be exported into request context', max_length=100)),
                ('title', models.CharField(help_text=b'Title, verbose name / short description', max_length=100, blank=True)),
                ('body', models.TextField(help_text=b'Body of snippet, available via {{ &lt;name&gt; }} in templates')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'date updated')),
                ('published', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
