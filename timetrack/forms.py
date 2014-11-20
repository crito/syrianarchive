from django.db import models
from django import forms
from django.forms import ModelForm, Select
from timetrack.models import * 
from profiles.models import Profile
from projects.models import Project, Activity
from django.contrib.auth.models import User
from django.contrib.admin import widgets
import datetime


class EntryForm(ModelForm):
	class Meta:
		model = Entry
		exclude = ['created','creator','creator_profile']
