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




def index(request):
    if request.user.is_authenticated():
        '''
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
        '''
        current_path = request.get_full_path()
        
        if request.GET.items():
            if request.method == "GET":
                form = DatabaseFilterForm(request.GET, request.FILES)

                if form.is_valid():
                #page = form.cleaned_data['page']
                    type_of_violation = form.cleaned_data['type_of_violation']
                    location = form.cleaned_data['location']


                
                    entries = DatabaseEntry.objects.filter(type_of_violation=type_of_violation).filter(location=location)
              
                else:
                    entries = DatabaseEntry.objects.all()

                    form = DatabaseFilterForm()
        else:
            form = DatabaseFilterForm()
            entries = DatabaseEntry.objects.all()
    
        
        return render(request, 'database/index.html', {'entries': entries, 'form':form, "current_path":current_path})
	
    return render(request, 'database/loginrequired.html')






def detail(request, slug):
	if request.user.is_authenticated():
    		
    		incident = get_object_or_404(DatabaseEntry, pk=slug )
		return render(request, 'database/incident.html', {'incident': incident, 'slug':slug})
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