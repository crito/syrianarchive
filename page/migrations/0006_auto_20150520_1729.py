# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0005_pageblogpost_short_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='page.Page')),
                ('main_image', models.ImageField(null=True, upload_to=b'blog_images', blank=True)),
                ('short_description', models.TextField(max_length=500, null=True, blank=True)),
            ],
            bases=('page.page',),
        ),
        migrations.RemoveField(
            model_name='pageblogpost',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='PageBlogPost',
        ),
    ]
