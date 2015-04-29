# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0002_auto_20150429_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='databaseentry',
            name='gender_or_sex',
            field=models.NullBooleanField(),
        ),
    ]
