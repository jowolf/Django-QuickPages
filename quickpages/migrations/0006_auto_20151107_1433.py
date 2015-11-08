# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0005_auto_20151107_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='quicksnippet',
            name='comments',
            field=models.TextField(help_text=b'Internal developer/editor comments, not shown', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='quicksnippet',
            name='typ',
            field=models.TextField(help_text=b'Editor type - raw, html, etc - future: Markdown, etc', blank=True, choices=[(b'raw', b'Raw - passed thru as is'), (b'html', b'HTML - Use the built-in HTML Editor (warning: will strip certain tags, etc')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='quicksnippet',
            name='css',
            field=models.TextField(help_text=b'CSS for this snippet - &lt;link&gt; tags will be passed through', blank=True),
            preserve_default=True,
        ),
    ]
