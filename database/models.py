from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from datetime import datetime
import time

# Create your models here.
'''
    	-Reference Code
    	-Staff ID
    	-Date
    	-Creator
    	-File Name
    	-Recording Date and Time
    	-Location
    	-Summary
    	-Generation
    	-Existence & Location of Original
    	-Edited? (Y/N)
    	-Is this footage online? (Y/N)
    	-Online link
    	-Online title
    	-File Size
    	-Duration
    	-Date of acquisition
    	-Acquired from
    	-Chain of Custody Notes
    	-Date of fixity check
    	-MD5 hash value
    	-Content Type
    	-Language(s)
    	-Finding Aids
    	-Is there graphic content? (Y/N)
    	-Security Restriction Status
    	-Rights owner
   		-Rights declaration
    	-Creator willing to be a witness in case
    	footage is used as evidence for a legal
    	case? (Y/N)
    	-Priority of the footage
    	-Keywords
    -Notes
    '''

class DatabaseEntry(models.Model):
	name = models.CharField(max_length=250)

	reference_code = models.CharField(max_length=250, null=True, blank=True)
	staff_id = models.CharField(max_length=250, null=True, blank=True)
	file_name = models.CharField(max_length=250, null=True, blank=True)
	description = models.TextField(max_length=5000, null=True, blank=True)
	recording_date = models.DateTimeField(default=datetime.now, auto_now_add=True, null=True, blank=True)
	location_name = models.CharField(max_length=250, null=True, blank=True)
	location_latitude = models.CharField(max_length=250, null=True, blank=True)
	location_longitude = models.CharField(max_length=250, null=True, blank=True)
	generation = models.CharField(max_length=250, null=True, blank=True)
	location_of_original = models.CharField(max_length=250, null=True, blank=True)
	edited = models.NullBooleanField(null=True, blank=True)
	online = models.NullBooleanField(null=True, blank=True)
	online_link = models.CharField(max_length=250, null=True, blank=True)
	online_title = models.CharField(max_length=250, null=True, blank=True)
	file_size = models.CharField(max_length=250, null=True, blank=True)
	duration = models.CharField(max_length=250, null=True, blank=True)
	date_of_acquisition = models.DateField(default=datetime.now)
	acquired_from = models.CharField(max_length=250, null=True, blank=True)
	chain_of_custody_notes = models.TextField(max_length=5000, null=True, blank=True)
	date_of_fixity_check = models.DateField(default=datetime.now)
	md5_hash = models.CharField(max_length=25000, null=True, blank=True)
	content_type = models.CharField(max_length=250, null=True, blank=True)
	languages = models.CharField(max_length=250, null=True, blank=True)
	finding_aids = models.CharField(max_length=250, null=True, blank=True)
	graphic_content = models.NullBooleanField(null=True, blank=True)
	security_restriction_status = models.CharField(max_length=250, null=True, blank=True)
	rights_owner = models.CharField(max_length=250, null=True, blank=True)
	rights_declaration = models.CharField(max_length=250, null=True, blank=True)
	creator_willing_witness = models.NullBooleanField(null=True, blank=True)
	priority = models.CharField(max_length=250, null=True, blank=True)
	keywords = models.CharField(max_length=250, null=True, blank=True)
	notes = models.TextField(max_length=5000, null=True, blank=True)


	added_date = models.DateField(default=datetime.now)

	creator = models.ForeignKey(User, null=True, blank=True)

	def __unicode__(self):
		return self.name
	def getCreatorID(self):
		if self.creator:
			return self.creator.username
		else:
			return 'ghost user'

	def to_json_dict(self):
		data = {
		'id' : self.id,
		'title': self.name,
		}
		return data

	def save(self, *args, **kwargs):
		super(DatabaseEntry, self).save(*args, **kwargs)
