# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='name_ar',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='internationalinstrument',
            name='name_ar',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='internationalinstrument',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='name_ar',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='locationplace',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='sourceconnection',
            name='name_ar',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='sourceconnection',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='violationtype',
            name='name_ar',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='violationtype',
            name='name_en',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
