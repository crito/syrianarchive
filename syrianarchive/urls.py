from django.conf.urls import patterns, include, url

from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^$', 'homepage.views.index', name='home'),
    url(r'^home/', include('homepage.urls')),
    url(r'^database/', include('database.urls')),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^docs/', include('docs.urls')),
    #url(r'^accounts/', include('profiles.urls')),
)