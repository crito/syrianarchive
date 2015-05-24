# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0006_auto_20150524_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='collections',
            field=models.ManyToManyField(to='database.Collection', blank=True),
        ),
    ]
