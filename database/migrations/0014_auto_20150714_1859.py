# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0013_auto_20150711_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationplace',
            name='dataset_id',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='geom',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='latitude',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='longitude',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='region',
            field=models.ForeignKey(blank=True, to='database.LocationPlace', null=True),
        ),
    ]
