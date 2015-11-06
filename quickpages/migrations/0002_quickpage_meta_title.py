# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quickpage',
            name='meta_title',
            field=models.TextField(help_text=b'Meta title', blank=True),
            preserve_default=True,
        ),
    ]
