# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_blogpost_main_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogPost',
            new_name='PageBlogPost',
        ),
    ]
