from django.db import models
from django import forms
from django.forms import ModelForm, Select
from django.contrib.auth.models import User
from datetime import datetime
import time
from profiles.models import Profile
import reversion
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Doc(models.Model):
	name = models.CharField(max_length=250)
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
		super(Doc, self).save(*args, **kwargs)





reversion.register(Doc)

class Group(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=5000, null=True, blank=True)
	docs = models.ManyToManyField(Doc, null=True, blank=True, related_name='groups')
	def __unicode__(self):
		return self.name


class GroupForm(ModelForm):	
	class Meta:
		model = Group
		exclude = ['creator', 'creator_profile', 'created']



class DocFile(models.Model):
	name = models.CharField(max_length=520)
	docfile = models.FileField(blank=True, upload_to='docfiles')
	doc = models.ForeignKey(Doc, null=True, blank=True)
	def __unicode__(self):
		return self.name


class DocFileForm(ModelForm):

	class Meta:
		model = DocFile
		exclude = ['doc']

class DocForm(ModelForm):
	comment = forms.CharField(max_length=250)
	groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
    )

	class Meta:
		model = Doc
		exclude = ['creator', 'creator_profile', 'created']


