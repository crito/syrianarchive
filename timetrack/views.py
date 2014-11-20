from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from timetrack.models import *
from forms import EntryForm
import json
from django.http import HttpResponse
from django.core import serializers

@login_required
def index(request):
	#latest_entries = Entry.objects.all().order_by('-created')
	currentuser = request.user
	currentprofile = currentuser.profile_set.filter()[:1].get()
	latest_entries = currentprofile.entry_set.all().order_by('-created')[:50]

	projects = currentprofile.project_set.all()

	for project in projects:
		project.activitieslist = project.activity_set.all()

	return render(request, 'timetrack/tracker/index.html', {
		'latest_entries' : latest_entries,
		'profile' : currentprofile,
		'projects' : projects,
		})

def entries_list(request):
	currentuser = request.user
	currentprofile = currentuser.profile_set.filter()[:1].get()
	latest_entries = currentprofile.entry_set.all().order_by('-created')
	#latest_entries = Entry.objects.all().order_by('-created')
	return render(request, 'timetrack/tracker/entries_list.html', {'latest_entries' : latest_entries})

@login_required
def add(request):
	if request.POST:
		form = EntryForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			activity = form.cleaned_data['activity']
			project = form.cleaned_data['project']
			date = form.cleaned_data['date']
			hours = form.cleaned_data['hours']
			user = request.user
			currentprofile = user.profile_set.filter()[:1].get()
			entry = Entry.objects.create(
				name = name, 
				description = description, 
				activity = activity, 
				project = project, 
				creator=user, 
				creator_profile=currentprofile,
				date=date,
				hours=hours,
				)
			entry.project = entry.activity.parent_project
			entry.save()
			if request.is_ajax():
				return render(request, 'timetrack/tracker/index.html')
			else:
				return HttpResponseRedirect('/time')
	else:
		form = EntryForm()
	return render(request, 'timetrack/tracker/add.html', {'form':form})

@login_required
def remove(request, entry_id):
	project = get_object_or_404(Entry, pk=entry_id)
	project.delete()
	return HttpResponseRedirect('/time')

@login_required
def calendar(request):
	currentuser = request.user
	currentprofile = currentuser.profile_set.filter()[:1].get()
	latest_entries = currentprofile.entry_set.all().order_by('-created')
	projects = currentprofile.project_set.all()
	for project in projects:
		project.activitieslist = project.activity_set.all()
	return render(request, 'timetrack/calendar/calendar.html', {
		'latest_entries' : latest_entries,
		'profile' : currentprofile,
		'projects' : projects,
		})

@login_required
def calendar_list(request):
	currentuser = request.user
	currentprofile = currentuser.profile_set.filter()[:1].get()
	latest_entries = currentprofile.entry_set.all().order_by('-created')
	#latest_entries = Entry.objects.all().order_by('-created')
	response_data = {}
	response_data['result'] = [mm.to_json_dict() for mm in latest_entries]
	response_data['message'] = 'yay'
	response_data['success'] = 1
	return HttpResponse(json.dumps(response_data), content_type="application/json")
