from django.shortcuts import get_object_or_404, render
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


# Create your views here.
'''
def user(request):
	if request.user.is_authenticated():
		authenticated = yes
	else: 
		authenticated = no

	return authenticated


class IndexView(generic.TemplateView):

	template_name = "database/index.html"


	def get_context_data(self, **kwargs):

	
		context = super(IndexView, self).get_context_data(**kwargs)
		context['entries'] = DatabaseEntry.objects.all()
		context['violationfilter'] = DatabaseFilterViolation(queryset=ViolationType.objects.all())
		context['locationfilter'] = DatabaseFilterLocation(queryset=LocationPlace.objects.all())
		return context


'''

def index(request):
	if request.user.is_authenticated():
		entries = DatabaseEntry.objects.all()
		violationfilter = DatabaseFilterViolation(request.GET, queryset=ViolationType.objects.all())
		locationfilter = DatabaseFilterLocation(request.GET, queryset=LocationPlace.objects.all())

		return render(request, 'database/index.html',{'entries':entries,'violationfilter':violationfilter,'locationfilter':locationfilter,})
	return render(request, 'database/loginrequired.html')

