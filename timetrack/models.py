from django.db import models
from django import forms
from profiles.models import Profile
from projects.models import Project, Activity
from django.contrib.auth.models import User
from django.contrib.admin import widgets
from datetime import datetime
import time

class Entry(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=5000, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	date = models.DateField(default=datetime.now)
	creator = models.ForeignKey(User, null=True, blank=True)
	creator_profile = models.ForeignKey(Profile, null=True, blank=True)
	activity = models.ForeignKey(Activity, null=True, blank=True)
	project = models.ForeignKey(Project, null=True, blank=True)
	hours = models.IntegerField(default=0)

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
		'url' : '/time/entry/'+str(self.id),
		'hours' : self.hours,
		'class' : 'event-important',
		'start' : int(time.mktime((self.date).timetuple())*1000),
		'end' : int(time.mktime((self.date).timetuple())*1000)
		}
		return data

	def save(self, *args, **kwargs):
		super(Entry, self).save(*args, **kwargs)
