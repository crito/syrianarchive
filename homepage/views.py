from homepage.models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required




# Create your views here.



def index(request, lang='en'):
	announcements = Section.objects.all()
	links = FrontPageLink.objects.all()
	return render(request, 'homepage/index.html', {'announcements' : announcements, 'links':links,'lang':lang,})

