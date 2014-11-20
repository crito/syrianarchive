from django.db import models
from django.db import models
from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from profiles.models import Profile
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Announcement(models.Model):
	description = models.TextField(max_length=5000, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	creator = models.ForeignKey(User, null=True, blank=True)
	creator_profile = models.ForeignKey(Profile, null=True, blank=True)

	def __unicode__(self):
		return self.name
	def getCreatorID(self):
		if self.creator:
			return self.creator.username
		else:
			return 'ghost user'

	def save(self, *args, **kwargs):
		super(Announcement, self).save(*args, **kwargs)


class AnnouncementForm(ModelForm):
	class Meta:
		model = Announcement
		widgets = {
            'description': SummernoteWidget(),
        }
		exclude = ['creator', 'creator_profile', 'created']




class FrontPageLink(models.Model):
	name = models.CharField(max_length=250)
	image = models.ImageField(upload_to='frontpagelinks', max_length=100, null=True, blank=True)
	description = models.TextField(max_length=5000, null=True, blank=True)
	link = models.CharField(max_length=250, null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	creator = models.ForeignKey(User, null=True, blank=True)
	creator_profile = models.ForeignKey(Profile, null=True, blank=True)

	def __unicode__(self):
		return self.name
	def getCreatorID(self):
		if self.creator:
			return self.creator.username
		else:
			return 'ghost user'

	def save(self, *args, **kwargs):
		super(FrontPageLink, self).save(*args, **kwargs)

class FrontPageLinkForm(ModelForm):
	class Meta:
		model = FrontPageLink
		exclude = ['creator', 'creator_profile', 'created']
