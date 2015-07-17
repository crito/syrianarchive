from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
import time
import django_filters
from django.db.models.signals import post_save
from djgeojson.fields import PointField
from syrianarchive.site_settings import BASE_PATH
import json

from django.shortcuts import get_object_or_404, render


class InternationalInstrument(models.Model):
    name = models.CharField( max_length = 250)
    number = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class MediaContentType(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class SourceConnection(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class LocationPlace(models.Model):
    name        = models.CharField( max_length = 250)
    region      = models.ForeignKey("LocationPlace", null = True, blank = True)
    geom        = PointField(null = True, blank = True)
    latitude    = models.CharField( max_length=250 , null = True , blank = True )
    longitude   = models.CharField( max_length=250 , null = True , blank = True )
    dataset_id  = models.IntegerField( null = True , blank = True )

    def __unicode__(self):
        return self.name

def import_from_dataset():
    current_locations = LocationPlace.objects.all()
    print BASE_PATH
    with open( BASE_PATH + '/database/data/locations.json', 'rU') as f:
        locations = json.load(f)
        for location in locations:
            print location["name"]
            region = get_object_or_404(LocationPlace, name = location["name"])
            new_location = LocationPlace.objects.create(
                name_en = location["name"],
                name_ar = location["arabic_name"],
                region  = region,
                dataset_id = location["id"],
                latitude = location["latitude"],
                longitude = location["longitude"],
                )
            print new_location

class Device(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class ViolationType(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class DatabaseEntry(models.Model):
    '''
        Public Fields of the model - made for people to see
    '''
    LANGS = (
        ('AR','Arabic'),
        ('EN','English'),
        ('FR','French'),
        ('RU','Russian'),
        ('FA','Persian'),
    )

    name                           = models.CharField( max_length = 250)
    reference_code                 = models.CharField( max_length = 250, null = True, blank = True)
    cloths_and_uniforms            = models.CharField( max_length = 250, null = True, blank = True)
    description                    = models.TextField( max_length = 5000, null = True, blank = True, default = '')
    recording_date                 = models.DateTimeField(default = datetime.now, null = True, blank = True)
    location_latitude              = models.CharField( max_length = 250, null = True, blank = True)
    location_longitude             = models.CharField( max_length = 250, null = True, blank = True)
    geom                           = PointField(null = True, blank = True)
    edited                         = models.NullBooleanField(null = True, blank = True)
    file_size                      = models.CharField( max_length = 250, null = True, blank = True)
    duration                       = models.CharField( max_length = 250, null = True, blank = True)
    chain_of_custody_notes_public  = models.TextField( max_length = 5000, null = True, blank = True)
    languages                      = models.CharField( max_length = 250, null = True, blank = True, choices=LANGS)
    finding_aids                   = models.CharField( max_length = 250, null = True, blank = True)
    graphic_content                = models.NullBooleanField(null = True, blank = True)
    gender_or_sex                  = models.NullBooleanField(null = True, blank = True)
    keywords                       = models.CharField( max_length = 250, null = True, blank = True)
    international_instrument_notes = models.TextField( max_length = 5000, null = True, blank = True)
    landmarks                      = models.TextField( max_length = 5000, null = True, blank = True)
    weather_in_media               = models.TextField( max_length = 5000, null = True, blank = True)
    weapons_used                   = models.TextField( max_length = 5000, null = True, blank = True)
    urls_and_news                  = models.TextField( max_length = 5000, null = True, blank = True)

    related_incidents              = models.ManyToManyField("DatabaseEntry", blank = True)
    type_of_violation              = models.ManyToManyField(ViolationType, blank = True)
    location                       = models.ManyToManyField(LocationPlace, blank = True)
    device_used                    = models.ManyToManyField(Device, blank = True)
    media_content_type             = models.ManyToManyField(MediaContentType,  blank = True)
    international_instrument       = models.ManyToManyField(InternationalInstrument, blank = True)

    reliability_score              = models.IntegerField(
                                         default = 1,
                                         validators=[
                                             MaxValueValidator(100),
                                             MinValueValidator(1)
                                         ]
                                        )

    '''
        private fields - only for site editors
    '''
    staff_id                        = models.CharField( max_length = 250, null = True, blank = True)
    file_name                       = models.CharField( max_length = 250, null = True, blank = True)
    recording_creator               = models.CharField( max_length = 250, null = True, blank = True)
    generation                      = models.CharField( max_length = 250, null = True, blank = True)
    location_of_original            = models.CharField( max_length = 250, null = True, blank = True)
    online                          = models.NullBooleanField(null = True, blank = True)
    online_link                     = models.CharField( max_length = 250, null = True, blank = True)
    online_link_mediadrop           = models.CharField( max_length = 250, null = True, blank = True)
    online_title                    = models.CharField( max_length = 250, null = True, blank = True)
    date_of_acquisition             = models.DateField( default = datetime.now)
    acquired_from                   = models.CharField( max_length = 250, null = True, blank = True)
    chain_of_custody_notes          = models.TextField( max_length = 5000, null = True, blank = True)
    STATUS                          = (
                                        ('R', 'Restricted'),
                                        ('U', 'Unrestricted'),
                                    )
    security_restriction_status     = models.CharField( max_length = 250, null = True, blank = True, choices=STATUS)
    security_restriction_notes      = models.TextField( max_length = 5000, null = True, blank = True)
    date_of_fixity_check            = models.DateTimeField(default = datetime.now, null = True, blank = True)
    md5_hash                        = models.CharField( max_length = 25000, null = True, blank = True)
    rights_owner                    = models.CharField( max_length = 250, null = True, blank = True)
    rights_declaration              = models.CharField( max_length = 250, null = True, blank = True)
    creator_willing_witness         = models.NullBooleanField(null = True, blank = True)
    PRIORITY_LIST                   = (
                                        ('UR', 'Urgent'),
                                        ('HP', 'High priority'),
                                        ('P', 'Priority'),
                                        ('LP', 'Low Priority'),
                                        ('CR', 'Case Rejected'),
                                    )
    priority                        = models.CharField( max_length = 250, null = True, blank = True, choices=PRIORITY_LIST)
    notes                           = models.TextField( max_length = 5000, null = True, blank = True)
    added_date                      = models.DateField(default = datetime.now)
    source_connection               = models.ManyToManyField(SourceConnection, blank = True)
    creator                         = models.ForeignKey(User, null = True, blank = True)

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        data = {
            'id' : self.id,
            'title': self.name,
        }
        return data

    def save(self, *args, **kwargs):
        super(DatabaseEntry, self).save(*args, **kwargs)





class Collection(models.Model):
    name            = models.CharField( max_length = 250)
    description     = models.CharField( max_length = 8000, null = True, blank = True)
    image           = models.ImageField(upload_to="collection_images", null = True, blank = True)

class Video(models.Model):
    name            = models.CharField( max_length = 250, default = "Add Name")
    source          = models.CharField( max_length = 250, null = True, blank = True)
    url             = models.CharField( max_length = 2000)     #filename is url
    database_entry  = models.OneToOneField(DatabaseEntry, related_name="video", blank = True, null = True)
    thumbnail       = models.ImageField(upload_to="thumbnails", null = True, blank = True)
    collections     = models.ManyToManyField(Collection, blank = True)

    def __unicode__(self):
        return self.url

def create_database_entry(sender, instance, created, **kwargs):
    ''' if the database entry was not added for the video, create a new one!'''
    if instance and created:
        video       = instance
        db_entry    = video.database_entry
        try:
            db_entry.name
        except:
            temp_db_entry = DatabaseEntry.objects.create(name=video.name)
            video.database_entry = temp_db_entry
            video.save()

post_save.connect(create_database_entry, sender=Video)