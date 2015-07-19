# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0018_auto_20150719_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='collections',
        ),
        migrations.RemoveField(
            model_name='video',
            name='database_entry',
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='collections',
            field=models.ManyToManyField(to='database.Collection', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'thumbnails', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='video_source',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='video_url',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
