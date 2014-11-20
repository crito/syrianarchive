from django.conf.urls import patterns, url
from docs import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add', views.add_doc),
    url(r'^group/(?P<group_id>\d+)$', views.group),
    url(r'^(?P<doc_id>\d+)/editor$', views.editor_doc, name='editor'),
    url(r'^(?P<doc_id>\d+)/edit$', views.edit_doc, name='edit'),
    url(r'^(?P<doc_id>\d+)/remove$', views.remove_doc, name='remove'),
    url(r'^(?P<doc_id>\d+)/files$', views.files, name='files'),
    url(r'^(?P<doc_id>\d+)/file/upload$', views.upload_file, name='upload'),
    url(r'^(?P<doc_id>\d+)/$', views.detail, name='detail'),

)