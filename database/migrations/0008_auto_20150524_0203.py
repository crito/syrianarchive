# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0007_video_collections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='database_entry',
            field=models.OneToOneField(related_name='video', null=True, blank=True, to='database.DatabaseEntry'),
        ),
    ]
