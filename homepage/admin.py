from django.contrib import admin
from django import forms
from homepage.models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor.widgets import CKEditorWidget

class SectionAdminForm(forms.ModelForm):
    description_en = forms.CharField(widget=CKEditorWidget())
    description_ar = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Section
        fields = "__all__" 

class SectionAdmin(TranslationAdmin):
    form = SectionAdminForm
    class Media:
        js = (
			'//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
			'//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
			'modeltranslation/js/tabbed_translation_fields.js',
		)
        css = {
			'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
		}



admin.site.register(Section, SectionAdmin)