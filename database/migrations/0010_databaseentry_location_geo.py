# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0009_video_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseentry',
            name='location_geo',
            field=djgeojson.fields.PointField(null=True, blank=True),
        ),
    ]
