from django.contrib import admin
from homepage.models import *
from django_summernote.admin import SummernoteModelAdmin



@admin.register(Section)
class SectionAdmin(SummernoteModelAdmin):
	pass

@admin.register(FrontPageLink)
class FrontPageLinkAdmin(SummernoteModelAdmin):
	pass
