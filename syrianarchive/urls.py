from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView

from page.views import blog

from syrianarchive.views import *

from django.contrib import admin
import settings

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'homepage.views.index', name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^blog/', 'page.views.blog', name='blog'),
    url(r'^accounts/login', TemplateView.as_view(template_name='loginrequired.html')),
    url(r'^home/', include('homepage.urls')),
    url(r'^p/', include('page.urls')),
    url(r'^database/', include('database.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),



)

