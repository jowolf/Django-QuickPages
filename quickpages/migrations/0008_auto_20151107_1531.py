# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0007_auto_20151107_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicksnippet',
            name='typ',
            field=models.CharField(default=b'raw', help_text=b'Editor type - raw, html, etc - future: Markdown, etc', max_length=20, choices=[(b'raw', b'Raw - passed thru as is'), (b'html', b'HTML - Use the built-in HTML Editor (warning: will strip certain tags, etc')]),
            preserve_default=True,
        ),
    ]
