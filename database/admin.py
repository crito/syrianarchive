from django.contrib import admin
from database.models import *
from django_summernote.admin import SummernoteModelAdmin
from django.forms import CheckboxSelectMultiple

@admin.register(InternationalInstrument)
class InternationalInstrumentEntryAdmin(admin.ModelAdmin):
	pass

@admin.register(MediaContentType)
class MediaContentTypeAdmin(admin.ModelAdmin):
	pass

@admin.register(SourceConnection)
class SourceConnectionAdmin(admin.ModelAdmin):
	pass

@admin.register(DatabaseEntry)
class DatabaseEntryAdmin(SummernoteModelAdmin):
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
	list_display = ('name', 
		'graphic_content',
		'staff_id',
		'recording_date',
		'online',
		'location_name',
		'priority',
		)
	fieldsets = (
        ('Required Fields', {
            'fields': ('name',)
        }),
        ('Public Fields', {
            'fields': (
            	'description',
            	'reference_code', 
            	'recording_date',
            	'location_name', 
            	('location_latitude','location_longitude',),
            	'edited',	
            	('file_size','duration',),
            	'chain_of_custody_notes_public',
            	'media_content_type',
            	'languages',
            	'finding_aids',
            	'graphic_content',
            	'keywords',
            	'international_instrument',
            	'landmarks',
            	'weather',
            )
        }),
        ('Private Fields', {
            'fields': (
            	'staff_id',
            	'file_name',
            	'recording_creator',
            	'generation',
            	'location_of_original',
            	'online',
            	'online_link',
            	'online_title',
            	'date_of_acquisition',
            	'acquired_from',
            	'chain_of_custody_notes',
            	'security_restriction_status',
            	'security_restriction_notes',
            	'date_of_fixity_check',
            	'md5_hash',
            	'rights_owner',
            	'rights_declaration',
            	'creator_willing_witness',
            	'priority',
            	'notes',
            	'source_connection',
            	'added_date',
            	'creator',
            	)
        }),

    )
    
	def save_model(self, request, obj, form, change):
		if not change:
			obj.creator = request.user
		obj.save()
