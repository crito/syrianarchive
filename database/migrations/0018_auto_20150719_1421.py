# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_auto_20150719_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databaseentry',
            name='device_used',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='device_used',
            field=models.ForeignKey(blank=True, to='database.Device', null=True),
        ),
        migrations.RemoveField(
            model_name='databaseentry',
            name='media_content_type',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='media_content_type',
            field=models.ForeignKey(blank=True, to='database.MediaContentType', null=True),
        ),
        migrations.RemoveField(
            model_name='databaseentry',
            name='source_connection',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='source_connection',
            field=models.ForeignKey(blank=True, to='database.SourceConnection', null=True),
        ),
        migrations.RemoveField(
            model_name='databaseentry',
            name='type_of_violation',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='type_of_violation',
            field=models.ForeignKey(blank=True, to='database.ViolationType', null=True),
        ),
    ]
