from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from .models import *
import time


# Create your views here.

@login_required
def index(request):
	
	entries = DatabaseEntry.objects.all()
	
	return render(request, 'database/index.html',{'entries':entries,})
