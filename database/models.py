from django.db import models
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
import time
import django_filters
from django.db.models.signals import post_save
from djgeojson.fields import PointField, PolygonField
import json


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
    region_geom = PolygonField(null = True, blank = True )
    latitude    = models.CharField( max_length=250 , null = True , blank = True )
    longitude   = models.CharField( max_length=250 , null = True , blank = True )
    dataset_id  = models.IntegerField( null = True , blank = True )

    def __unicode__(self):
        selfidentify = self.region.name + " : " + self.name
        return selfidentify

    def lat_lon_fields_to_geom(self):
        geofield = {'type': 'Point', 'coordinates': [float(self.longitude), float(self.latitude)]}
        self.geom = geofield



class Device(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name

class ViolationType(models.Model):
    name = models.CharField( max_length = 250)

    def __unicode__(self):
        return self.name



class Collection(models.Model):
    name            = models.CharField( max_length = 250)
    description     = models.CharField( max_length = 8000, null = True, blank = True)
    image           = models.ImageField(upload_to="collection_images", null = True, blank = True)

    def __unicode__(self):
      return self.name

class DatabaseEntry(models.Model):
    '''
        video fields
    '''
    video_source          = models.CharField( max_length = 250, null = True, blank = True)
    video_url             = models.CharField( max_length = 2000, null = True, blank = True)     #filename is url
    thumbnail       = models.ImageField(upload_to="thumbnails", null = True, blank = True)
    collections     = models.ManyToManyField(Collection, blank = True)


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
    type_of_violation              = models.ForeignKey(ViolationType, null = True, blank = True)
    location                       = models.ForeignKey(LocationPlace, null = True, blank = True)
    device_used                    = models.ForeignKey(Device, null = True, blank = True)
    media_content_type             = models.ForeignKey(MediaContentType, null=True,  blank = True)
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
    source_connection               = models.ForeignKey(SourceConnection, null = True, blank = True)
    creator                         = models.ForeignKey(User, null = True, blank = True)

    def __unicode__(self):
        return self.name

    def to_json_dict(self):
        data = {
            'id' : self.id,
            'title': self.name,
        }
        return data

    @property
    def popupcontent(self):
      htmlcontent = '''
      <div class="popupmodel">
        <a href="/database/%(id)s" target="_blank">%(refcode)s</a>
        <small>%(recording_date)s</small>
        <br />
        <strong><small>%(violation)s</small></strong>
        <p>%(description)s</p>
      </div>
        ''' % {
        'id':self.pk,
        'refcode':self.reference_code,
        'recording_date':self.recording_date,
        'description':self.description,
        'violation':self.type_of_violation,
        }
      return htmlcontent

    @property
    def violation(self):
      return self.type_of_violation.name

    def get_location_field(self):
        if self.geom != None:
            print "here1"
            return json.dumps(self.geom)
        else:
            print "here2"
            if self.location != None:
                print "here3"
                print json.dumps(self.location.geom)
                return json.dumps(self.location.geom)

    def save(self, *args, **kwargs):
        super(DatabaseEntry, self).save(*args, **kwargs)





