from django.contrib import admin
from docs.models import *
import reversion



class DocAdmin(reversion.VersionAdmin):

    pass

admin.site.register(Doc, DocAdmin)
admin.site.register(DocFile)
admin.site.register(Group)

# Register your models here.
