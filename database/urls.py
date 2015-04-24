from django.conf.urls import patterns, url
from database import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^(?P<slug>[0-9]+)/$', views.detail, name='detail')
)

