# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FrontPageLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(null=True, upload_to=b'frontpagelinks', blank=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('link', models.CharField(max_length=250, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_ar', models.CharField(max_length=250, null=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('description_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('description_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('arabic_name', models.CharField(max_length=250, null=True, blank=True)),
                ('arabic_description', models.TextField(max_length=5000, null=True, blank=True)),
            ],
        ),
    ]
