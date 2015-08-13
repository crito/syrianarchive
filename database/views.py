from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from django.views import generic
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .forms import *
import time
from haystack.query import SearchQuerySet
from djgeojson.views import GeoJSONLayerView




@login_required
def index(request):
    current_path = request.get_full_path()

    if request.method == "GET" and request.GET.items():
        form = DatabaseFilterForm(request.GET, request.FILES)
        if form.is_valid():
            type_of_violation = form.cleaned_data['type_of_violation']
            location = form.cleaned_data['location']
            start_date = form.cleaned_data['startDate']
            end_date = form.cleaned_data['endDate']

            kwargs = {}
            if type_of_violation:
                kwargs['type_of_violation'] = type_of_violation
            if location:
                kwargs['location'] = location
            if start_date and end_date:
                kwargs['recording_date__range'] = (start_date, end_date)

            entries = DatabaseEntry.objects.all().filter(**kwargs)


        else:
            entries = DatabaseEntry.objects.all()
            form = DatabaseFilterForm(request.GET, request.FILES)

    else:
        entries = DatabaseEntry.objects.all()
        form = DatabaseFilterForm(request.GET, request.FILES)

    return render(request, 'database/index.html', {'entries': entries, 'form':form, "current_path":current_path})

@login_required
def detail(request, slug):
    incident = get_object_or_404(DatabaseEntry, pk=slug )
    geofield = incident.get_location_field()
    return render(request, 'database/incident.html', {'incident': incident, 'slug':slug,'geofield':geofield})

@login_required
def collections(request):
    collections = Collection.objects.all()
    return render(request, 'database/collections.html', {'collections':collections})

@login_required
def collection(request, id):
    collection = get_object_or_404(Collection, pk=id)
    videos = collection.databaseentry_set.all()
    return render(request, 'database/collection.html', {'collection':collection, 'videos':videos})


class MapLayer(GeoJSONLayerView):

  def get_queryset(self):
      print self.request
      if self.request.method == "GET" and self.request.GET.items():
        print "yea"
      context = DatabaseEntry.objects.all()
      return context

def map(request):

  violationtypes = ViolationType.objects.all()
  return render(request, 'database/map.html',{'violationtypes':violationtypes,})