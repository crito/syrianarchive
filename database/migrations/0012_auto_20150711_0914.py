# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0011_auto_20150601_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='source',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='databaseentry',
            name='description',
            field=models.TextField(default=b'', max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='databaseentry',
            name='description_ar',
            field=models.TextField(default=b'', max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='databaseentry',
            name='description_en',
            field=models.TextField(default=b'', max_length=5000, null=True, blank=True),
        ),
    ]
