from django.db import models
from django.forms import ModelForm
from django.forms.models import BaseModelFormSet
from django.contrib.auth.models import User
from datetime import datetime
import time
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Profile(models.Model):
    # Required fields, editable only by an administrator:
    user = models.ForeignKey(User, unique=True)		# a one-to-one relationship between Users and Profiles
    display_name = models.CharField(max_length=50)	
    # Optional fields
    contact = models.EmailField('Email (optional)', blank=True)
    website = models.URLField('Website (optional)', max_length=200, blank=True)
    location = models.CharField('Location (optional)', max_length=50, blank=True)
    biography = models.TextField('About (optional)', max_length=100000, blank=True)
    # Automatic fields
    modified = models.DateField('Last modified', auto_now=True, auto_now_add=True)
    
    def __unicode__(self):
        return self.display_name
    def getCreatorID(self):
        return self.user.username
    def hasContact(self):
        return len(self.contact) > 0
    def hasWebsite(self):
        return len(self.contact) > 0
    def hasLocation(self):
        return len(self.location) > 0
    def hasBiography(self):
        return len(self.biography) > 0
    #def canShareWriting(self):
     #   return self.can_post_articles or self.profile_type == 'L'

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        widgets = {
            'biography': SummernoteWidget(),
        }
        exclude = ['user']
