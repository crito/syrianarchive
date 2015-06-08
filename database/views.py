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
from .forms import *
import time
from pprint import pprint



@login_required
def index(request):
    current_path = request.get_full_path()

    if request.method == "GET" and request.GET.items():
        form = DatabaseFilterForm(request.GET, request.FILES)
        print request.GET.getlist('type_of_violation')
        if form.is_valid():
            type_of_violation = form.cleaned_data['type_of_violation']
            location = form.cleaned_data['location']
            start_date = form.cleaned_data['startDate']
            end_date = form.cleaned_data['endDate']
            page = form.cleaned_data['page']


            kwargs = {}
            print 'type of vio', type_of_violation
            if type_of_violation:
                kwargs['type_of_violation'] = type_of_violation
            print 'loc',location
            if location:
                kwargs['location'] = location
            print 'date', start_date, end_date
            if start_date and end_date:
                kwargs['recording_date__range'] = (start_date, end_date)

            entries = DatabaseEntry.objects.all()

            print 'page', page
            if page:
                page = page - 1
                entries = entries.filter(**kwargs)[page*50:page*50+50]
            else:
                entries = entries.filter(**kwargs)[0:50]

        else:
            print "NOOOPE"
            entries = DatabaseEntry.objects.all()
            form = DatabaseFilterForm(request.GET, request.FILES)
      
    else:
        entries = DatabaseEntry.objects.all()
        form = DatabaseFilterForm(request.GET, request.FILES)


    
    return render(request, 'database/index.html', {'entries': entries, 'form':form, "current_path":current_path})
	






def detail(request, slug):
    if request.user.is_authenticated():
        incident = get_object_or_404(DatabaseEntry, pk=slug )
        try:
            video = incident.video
        except:
            video = None
        return render(request, 'database/incident.html', {'incident': incident, 'slug':slug,'video':video})
    return render(request, 'database/loginrequired.html')

def collections(request):
    collections = Collection.objects.all()
    return render(request, 'database/collections.html', {'collections':collections})

def collection(request, id):
    collection = get_object_or_404(Collection, pk=id)
    videos = collection.video_set.all()
    return render(request, 'database/collection.html', {'collection':collection, 'videos':videos})


def map(request):
    return render(request, 'database/map.html',{})