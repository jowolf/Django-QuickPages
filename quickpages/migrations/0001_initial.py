# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuickPage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(help_text=b'This is the url. Slashes are OK, but not necessary.', unique=True, max_length=1024)),
                ('name', models.CharField(help_text=b'Name - short, typically one or two words.', max_length=512)),
                ('title', models.CharField(help_text=b'Page title, and optional H1 tag (see Heading)', max_length=512)),
                ('published', models.BooleanField(default=True, help_text=b'Published=shown. If not, gives 404')),
                ('javascript', models.CharField(help_text=b'Comma-separated filenames, relative to MEDIA_ROOT or STATIC_ROOT', max_length=1024, blank=True)),
                ('css', models.CharField(help_text=b'Comma-separated filenames, relative to MEDIA_ROOT or STATIC_ROOT', max_length=1024, blank=True)),
                ('heading', models.BooleanField(default=True, help_text=b'If "Heading" is checked, "Title" is added to the top of the content in an H1 tag.')),
                ('description', models.TextField(help_text=b'Meta description', blank=True)),
                ('keywords', models.TextField(help_text=b'Meta keywords', blank=True)),
                ('comments', models.TextField(help_text=b'Internal developer/editor comments, not shown', blank=True)),
                ('content', models.TextField(help_text=b'HTML Content - main content div of the page.', blank=True)),
                ('template', models.CharField(help_text=b'Optional template - default is quickpages/base.html, which you can also simply replace in your project tree.', max_length=100, blank=True)),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'date modified')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        #migrations.CreateModel(
        #    name='QuickSnippet',
        #    fields=[
        #    ],
        #    options={
        #        'proxy': True,
        #    },
        #    bases=('obdjects.snippet',),
        #),
    ]
