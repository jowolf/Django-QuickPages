# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0002_quickpage_meta_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quickpage',
            name='meta_title',
            field=models.CharField(help_text=b'Meta title', max_length=512, blank=True),
            preserve_default=True,
        ),
    ]
