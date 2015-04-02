from django.contrib import admin
from homepage.models import *
from django_summernote.admin import SummernoteModelAdmin
from modeltranslation.admin import TranslationAdmin


class SectionAdmin(TranslationAdmin):
	class Media:
		js = (
			'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
		css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}

@admin.register(FrontPageLink)
class FrontPageLinkAdmin(SummernoteModelAdmin):
	pass

admin.site.register(Section, SectionAdmin)