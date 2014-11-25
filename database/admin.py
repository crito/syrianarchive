from django.contrib import admin
from database.models import *
from django_summernote.admin import SummernoteModelAdmin



@admin.register(DatabaseEntry)
class DatabaseEntryAdmin(SummernoteModelAdmin):
	list_display = ('name', 
		'graphic_content',
		'staff_id',
		'recording_date',
		'online',
		'content_type',
		'location_name',
		'priority',
		)
	def save_model(self, request, obj, form, change):
		if not change:
			obj.creator = request.user
		obj.save()
