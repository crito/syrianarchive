from django.shortcuts import render
from docs.models import *
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
import html2text
from django.utils.html import strip_tags


@login_required
def index(request):
	groups = Group.objects.all().order_by('name')
	latest_docs_list = Doc.objects.all().order_by('-created')[:30]
	return render(request, 'docs/docs/index.html', {'latest_docs_list' : latest_docs_list, 'groups':groups,})

@login_required
def detail(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	version_list = reversion.get_for_object(doc)[:10]
	return render(request, 'docs/docs/detail.html', {
		'doc' : doc,
		'version_list' : version_list,
		})

@login_required
def add_doc(request):

	name = "New Document"
	creator = request.user
	description = 'click to begin editing.  double click to add an image.'
	doc = Doc.objects.create(creator = creator, name = name, description=description)
	doc.save()
	return HttpResponseRedirect('/docs/'+str(doc.id)+'/editor')

@login_required
@transaction.atomic()
@reversion.create_revision()
def edit_doc(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	if request.method == 'POST':
		form = DocForm(request.POST, request.FILES, instance=doc)
		if form.is_valid():
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			formgroups = form.cleaned_data['groups']
			groups = Group.objects.all()
			for group in groups:
				if group in formgroups:
					group.docs.add(doc)
				else:
					group.docs.remove(doc)
			#h = html2text.HTML2Text()
			#h.ignore_links = True
			#description = h.handle(description)
			#description = strip_tags(description)
			#description=''

			comment = form.cleaned_data['comment']
			#doc.description = description
			doc.save()
			form.save()
			reversion.set_comment(comment)
			return HttpResponseRedirect('/docs/'+doc_id)
	form = DocForm(instance=doc)
	return render(request, 'docs/docs/edit.html', {'form':form,'doc_id':doc_id,'doc':doc,})

@login_required
@transaction.atomic()
@reversion.create_revision()
def editor_doc(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	files = doc.docfile_set.all()
	groups = Group.objects.all().order_by('name')
	for group in groups:
		if doc in group.docs.all():
			group.selected = True

	return render(request, 'docs/docs/editor.html', {'doc_id':doc_id,'doc':doc,'files':files,'groups':groups,})

@login_required
def remove_doc(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	if request.method == 'POST':
		doc.delete()
		return HttpResponseRedirect('/docs')
	else:
		name = doc.name
		return render(request, 'docs/docs/remove.html',{'doc_id':doc_id,'doc':doc,})

@login_required
def upload_file(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	if request.method == 'POST':
		form = DocFileForm(data=request.POST, files=request.FILES)
		if form.is_valid():
			instance = DocFile.objects.create(name=form.cleaned_data['name'],docfile=request.FILES['docfile'], doc=doc)
			instance.save()
			return HttpResponseRedirect(instance.docfile.url)
	else:
		form = DocFileForm()
	return render(request, 'docs/docs/uploadfile.html', {'form': form, 'doc':doc})


@login_required
def files(request, doc_id):
	doc = get_object_or_404(Doc, pk=doc_id)
	files = doc.docfile_set.all()
	return render(request, 'docs/docs/files.html', {'files':files})


@login_required
def group(request, group_id):
	group = get_object_or_404(Group, pk=group_id)
	docs = group.docs.all().order_by('-created')
	return render(request, 'docs/docs/group.html', {'docs':docs,'group':group})