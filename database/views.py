from django.shortcuts import get_object_or_404, render, render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from datetime import datetime, timedelta
from django_filters.views import FilterView
from django_filters.filterset import FilterSet, filterset_factory
from .models import *
import time



def index(request):
	if request.user.is_authenticated():
    		f = DatabaseFilter(request.GET, queryset=DatabaseEntry.objects.all())
    	
    		return render_to_response('database/index.html', {'filter': f})
	
	return render(request, 'database/loginrequired.html')

def detail(request, slug):
	if request.user.is_authenticated():
    		
    		incident = get_object_or_404(DatabaseEntry, pk=slug )
		return render(request, 'database/incident.html', {'incident': incident, 'slug':slug})
	return render(request, 'database/loginrequired.html')

