# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DatabaseEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_ar', models.CharField(max_length=250, null=True)),
                ('reference_code', models.CharField(max_length=250, null=True, blank=True)),
                ('cloths_and_uniforms', models.CharField(max_length=250, null=True, blank=True)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('description_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('description_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('recording_date', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('location_latitude', models.CharField(max_length=250, null=True, blank=True)),
                ('location_longitude', models.CharField(max_length=250, null=True, blank=True)),
                ('edited', models.NullBooleanField()),
                ('file_size', models.CharField(max_length=250, null=True, blank=True)),
                ('duration', models.CharField(max_length=250, null=True, blank=True)),
                ('chain_of_custody_notes_public', models.TextField(max_length=5000, null=True, blank=True)),
                ('chain_of_custody_notes_public_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('chain_of_custody_notes_public_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('languages', models.CharField(blank=True, max_length=250, null=True, choices=[(b'AR', b'Arabic'), (b'EN', b'English'), (b'FR', b'French'), (b'RU', b'Russian'), (b'FA', b'Persian')])),
                ('finding_aids', models.CharField(max_length=250, null=True, blank=True)),
                ('graphic_content', models.NullBooleanField()),
                ('keywords', models.CharField(max_length=250, null=True, blank=True)),
                ('international_instrument_notes', models.TextField(max_length=5000, null=True, blank=True)),
                ('international_instrument_notes_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('international_instrument_notes_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('landmarks', models.TextField(max_length=5000, null=True, blank=True)),
                ('landmarks_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('landmarks_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('weather_in_media', models.TextField(max_length=5000, null=True, blank=True)),
                ('weather_in_media_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('weather_in_media_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('weapons_used', models.TextField(max_length=5000, null=True, blank=True)),
                ('weapons_used_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('weapons_used_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('urls_and_news', models.TextField(max_length=5000, null=True, blank=True)),
                ('urls_and_news_en', models.TextField(max_length=5000, null=True, blank=True)),
                ('urls_and_news_ar', models.TextField(max_length=5000, null=True, blank=True)),
                ('staff_id', models.CharField(max_length=250, null=True, blank=True)),
                ('file_name', models.CharField(max_length=250, null=True, blank=True)),
                ('recording_creator', models.CharField(max_length=250, null=True, blank=True)),
                ('generation', models.CharField(max_length=250, null=True, blank=True)),
                ('location_of_original', models.CharField(max_length=250, null=True, blank=True)),
                ('online', models.NullBooleanField()),
                ('online_link', models.CharField(max_length=250, null=True, blank=True)),
                ('online_link_mediadrop', models.CharField(max_length=250, null=True, blank=True)),
                ('online_title', models.CharField(max_length=250, null=True, blank=True)),
                ('date_of_acquisition', models.DateField(default=datetime.datetime.now)),
                ('acquired_from', models.CharField(max_length=250, null=True, blank=True)),
                ('chain_of_custody_notes', models.TextField(max_length=5000, null=True, blank=True)),
                ('security_restriction_status', models.CharField(blank=True, max_length=250, null=True, choices=[(b'R', b'Restricted'), (b'U', b'Unrestricted')])),
                ('security_restriction_notes', models.TextField(max_length=5000, null=True, blank=True)),
                ('date_of_fixity_check', models.DateTimeField(default=datetime.datetime.now, null=True, blank=True)),
                ('md5_hash', models.CharField(max_length=25000, null=True, blank=True)),
                ('rights_owner', models.CharField(max_length=250, null=True, blank=True)),
                ('rights_declaration', models.CharField(max_length=250, null=True, blank=True)),
                ('creator_willing_witness', models.NullBooleanField()),
                ('priority', models.CharField(blank=True, max_length=250, null=True, choices=[(b'UR', b'Urgent'), (b'HP', b'High priority'), (b'P', b'Priority'), (b'LP', b'Low Priority'), (b'CR', b'Case Rejected')])),
                ('notes', models.TextField(max_length=5000, null=True, blank=True)),
                ('added_date', models.DateField(default=datetime.datetime.now)),
                ('creator', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='InternationalInstrument',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('number', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='LocationPlace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='MediaContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('name_en', models.CharField(max_length=250, null=True)),
                ('name_ar', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SourceConnection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ViolationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='device_used',
            field=models.ManyToManyField(to='database.Device', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='international_instrument',
            field=models.ManyToManyField(to='database.InternationalInstrument', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='location',
            field=models.ManyToManyField(to='database.LocationPlace', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='media_content_type',
            field=models.ManyToManyField(to='database.MediaContentType', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='source_connection',
            field=models.ManyToManyField(to='database.SourceConnection', blank=True),
        ),
        migrations.AddField(
            model_name='databaseentry',
            name='type_of_violation',
            field=models.ManyToManyField(to='database.ViolationType', blank=True),
        ),
    ]
