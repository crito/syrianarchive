# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='main_image',
            field=models.ImageField(null=True, upload_to=b'blog_images', blank=True),
        ),
    ]
