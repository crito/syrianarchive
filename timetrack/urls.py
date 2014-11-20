from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'timetrack.views.index', name='home'),
	url(r'^add', 'timetrack.views.add'),
	url(r'^entries_list', 'timetrack.views.entries_list'),
	url(r'^entry/(?P<entry_id>\d+)/remove$', 'timetrack.views.remove', name='remove'),
	url(r'^calendar', 'timetrack.views.calendar'),
	url(r'^api/calendar_list.json', 'timetrack.views.calendar_list'),
)