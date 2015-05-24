from django.conf.urls import patterns, url
from database import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^collection/(?P<id>[0-9]+)/$', views.collection, name='collection'),
	url(r'^(?P<slug>[0-9]+)/$', views.detail, name='detail')
)

