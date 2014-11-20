from homepage.models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required




# Create your views here.


@login_required
def index(request):
	announcements = Announcement.objects.all().order_by('-created')[:15]
	links = FrontPageLink.objects.all()
	return render(request, 'homepage/index.html', {'announcements' : announcements, 'links':links,})


@login_required
def add_announcement(request):
	if request.method == 'POST':
		form = AnnouncementForm(request.POST, request.FILES)
	else:
		form = AnnouncementForm()
	if form.is_valid():
		description = form.cleaned_data['description']
		creator = request.user
		announcement = Announcement.objects.create(creator = creator, description = description)
		announcement.save()
		return HttpResponseRedirect('/')
	return render(request, 'homepage/add_announcement.html', {'form':form,})



@login_required
def add_link(request):
	if request.method == 'POST':
		form = FrontPageLinkForm(request.POST, request.FILES)
	else:
		form = FrontPageLinkForm()
	if form.is_valid():
		description = form.cleaned_data['description']
		name = form.cleaned_data['name']
		link = form.cleaned_data['link']
		image = form.cleaned_data['image']
		creator = request.user
		frontpagelink = FrontPageLink.objects.create(name=name,link=link,image=image,creator = creator, description = description)
		frontpagelink.save()
		return HttpResponseRedirect('/')
	return render(request, 'homepage/add_link.html', {'form':form,})

