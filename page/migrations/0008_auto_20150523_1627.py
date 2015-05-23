# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0007_auto_20150520_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='short_description_ar',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='short_description_en',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
