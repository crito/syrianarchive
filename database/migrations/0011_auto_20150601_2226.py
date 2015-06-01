# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0010_databaseentry_location_geo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseentry',
            name='location_geo',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='geom',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
    ]
