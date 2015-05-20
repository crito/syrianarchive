# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0004_auto_20150520_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageblogpost',
            name='short_description',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
