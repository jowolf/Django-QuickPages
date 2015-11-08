# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0008_auto_20151107_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quicksnippet',
            name='body',
            field=models.TextField(help_text=b'Body of snippet, available via {{ &lt;name&gt; }} in templates via context processor'),
            preserve_default=True,
        ),
    ]
