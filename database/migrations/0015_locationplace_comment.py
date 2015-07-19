# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0014_auto_20150714_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationplace',
            name='comment',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
