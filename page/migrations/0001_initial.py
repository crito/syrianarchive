# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('title_en', models.CharField(max_length=250, null=True)),
                ('title_ar', models.CharField(max_length=250, null=True)),
                ('body', models.TextField(max_length=50000, null=True, blank=True)),
                ('body_en', models.TextField(max_length=50000, null=True, blank=True)),
                ('body_ar', models.TextField(max_length=50000, null=True, blank=True)),
                ('url', models.SlugField(max_length=250)),
                ('linked_pages', models.ManyToManyField(related_name='linked_pages_rel_+', null=True, to='page.Page', blank=True)),
            ],
        ),
    ]
