# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0005_auto_20150523_1732'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_ar', models.CharField(max_length=250, null=True)),
                ('description', models.CharField(max_length=8000, null=True, blank=True)),
                ('description_en', models.CharField(max_length=8000, null=True, blank=True)),
                ('description_ar', models.CharField(max_length=8000, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'collection_images', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(null=True, upload_to=b'thumbnails', blank=True),
        ),
    ]
