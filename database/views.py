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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
import time
from pprint import pprint



def index(request):
    if request.user.is_authenticated():
        f = DatabaseFilter(request.GET, queryset=DatabaseEntry.objects.all())
        paginator = Paginator(f,20)
        page = request.GET.get('page')
        try:
            entries = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            entries = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            entries = paginator.page(paginator.num_pages)

        pprint(f)

        current_path = request.get_full_path()

        print request.GET
        print f.form.as_p
        print f.qs
        
        return render(request, 'database/index.html', {'entries': entries, 'filter':f, "current_path":current_path})
	
    return render(request, 'database/loginrequired.html')

def detail(request, slug):
	if request.user.is_authenticated():
    		
    		incident = get_object_or_404(DatabaseEntry, pk=slug )
		return render(request, 'database/incident.html', {'incident': incident, 'slug':slug})
	return render(request, 'database/loginrequired.html')

