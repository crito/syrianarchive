# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='arabic_description',
        ),
        migrations.RemoveField(
            model_name='section',
            name='arabic_name',
        ),
    ]
