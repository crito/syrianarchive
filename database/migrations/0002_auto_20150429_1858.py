# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseentry',
            name='related_incidents',
            field=models.ManyToManyField(to='database.DatabaseEntry', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='reliability_score',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
        ),
    ]
