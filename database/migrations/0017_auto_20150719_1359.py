# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0016_auto_20150719_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseentry',
            name='location',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='location',
            field=models.ForeignKey(blank=True, to='database.LocationPlace', null=True),
        ),
    ]
