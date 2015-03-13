from django.db import models
from django.db import models
from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Section(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=5000, null=True, blank=True)
	arabic_name = models.CharField(max_length=250, null=True, blank=True)
	arabic_description = models.TextField(max_length=5000, null=True, blank=True)


	def __unicode__(self):
		return self.name
	def getCreatorID(self):
		if self.creator:
			return self.creator.username
		else:
			return 'ghost user'

	def save(self, *args, **kwargs):
		super(Section, self).save(*args, **kwargs)



class FrontPageLink(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='frontpagelinks', max_length=100, null=True, blank=True)
	description = models.TextField(max_length=5000, null=True, blank=True)
	link = models.CharField(max_length=250, null=True, blank=True)

	def __unicode__(self):
		return self.name
	def getCreatorID(self):
		if self.creator:
			return self.creator.username
		else:
			return 'ghost user'

	def save(self, *args, **kwargs):
		super(FrontPageLink, self).save(*args, **kwargs)

