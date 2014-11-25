from django.conf.urls import patterns, url
from database import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
)