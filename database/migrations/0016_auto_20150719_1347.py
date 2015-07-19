# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0015_locationplace_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locationplace',
            name='comment',
        ),
        migrations.AddField(
            model_name='locationplace',
            name='region_geom',
            field=djgeojson.fields.PolygonField(null=True, blank=True),
        ),
    ]
