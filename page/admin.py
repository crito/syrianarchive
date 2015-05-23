from django.contrib import admin
from django import forms
from page.models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor.widgets import CKEditorWidget


class PageAdminForm(forms.ModelForm):
    body_en = forms.CharField(widget=CKEditorWidget())
    body_ar = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Page
        fields = "__all__"


class PageAdmin(TranslationAdmin):
    form = PageAdminForm
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Page, PageAdmin)

class PostAdminForm(forms.ModelForm):
    body_en = forms.CharField(widget=CKEditorWidget())
    body_ar = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = "__all__"

class PostAdmin(TranslationAdmin):
    form = PostAdminForm
    class Media:
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            '//ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Post, PostAdmin)