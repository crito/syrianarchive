from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from profiles.models import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
import time

@login_required
def index(request):
	users = User.objects.all()
	users = list(users)
	profiles = Profile.objects.all().order_by('display_name')
	if not len(users) <= len(profiles):
		for profile in profiles:
			if profile.user in users:
				users.remove(profile.user)
		for user1 in users:
			display_name = user1.username
			userfk = user1
			profile1 = Profile.objects.create(display_name = display_name, user=userfk)
			profile1.save()
		profiles = Profile.objects.all().order_by('display_name')
	return render(request, 'profiles/index.html',{'profiles':profiles,})














@login_required
def detail(request, profile_id):
	profile = get_object_or_404(Profile, pk=profile_id)
	return profilepage(request, profile)

@login_required
def me(request):
	profile = get_object_or_404(Profile, user=request.user)
	return HttpResponseRedirect('/accounts/'+str(profile.id))
	#return profilepage(request, profile)

@login_required
def me_edit_account(request):
	profile = get_object_or_404(Profile, user=request.user)
	return edit_account(request, profile.id)

@login_required
def edit_account(request):
	profile = get_object_or_404(Profile, user=request.user)
	if request.method == 'POST':
		form = ProfileForm(request.POST, request.FILES, instance=profile)
		if form.is_valid():
			#name = form.cleaned_data['name']
			#description = form.cleaned_data['description']
			#project_code = form.cleaned_data['project_code']
			profile.save()
			return HttpResponseRedirect('/accounts/'+str(profile.id))
	form = ProfileForm(instance=profile)
	return render(request, 'profiles/edit.html', {'form':form,'profile_id':profile.id,'profile':profile,})

@login_required
def edit_contract(request, contract_id):
	contract = get_object_or_404(Contract, pk=contract_id)
	profile = contract.profile
	if request.method == 'POST':
		form = ContractForm(request.POST, request.FILES, instance=contract)
		if form.is_valid():
			#name = form.cleaned_data['name']
			#description = form.cleaned_data['description']
			#project_code = form.cleaned_data['project_code']
			contract.save()
			return HttpResponseRedirect('/accounts/'+ str(profile.id))
	form = ContractForm(instance=contract)
	return render(request, 'contracts/edit.html', {'form':form,'contract_id':contract_id,'contract':contract,'profile_name':profile.display_name,})
	
@login_required
def add_contract(request, profile_id):
	profile = get_object_or_404(Profile, pk=profile_id)
	if request.POST:
		form = ContractForm(request.POST)
		if form.is_valid():
			startdate = form.cleaned_data['startdate']
			enddate = form.cleaned_data['enddate']
			hours = form.cleaned_data['hours_per_week']
			profile = profile
			contract = Contract.objects.create(
				startdate = startdate, 
				enddate = enddate, 
				hours_per_week = hours, 
				profile = profile, 
				)
			contract.save()
			return HttpResponseRedirect('/accounts/'+profile_id)
	else:
		form = ContractForm()
	return render(request, 'contracts/add.html', {'form':form, 'profile_name':profile.display_name,'profile_id':profile_id,})


def loginuser(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(request.POST.get('pasta', False))
			else:
				return HttpResponseRedirect('/accounts/login')
		else:
			return HttpResponseRedirect('/accounts/login')
	else:
		noodle = request.GET.get('next', False)
		if noodle:
			return render(request, 'profiles/login.html', {'next':noodle,})
		else:
			return render(request, 'profiles/login.html', {'next':'/',})

def logoutuser(request):
	logout(request)
	return HttpResponseRedirect('/accounts/login')
