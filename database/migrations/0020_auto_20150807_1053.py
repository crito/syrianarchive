# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20150719_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseentry',
            name='acquired_from_ar',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='acquired_from_en',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
    ]
