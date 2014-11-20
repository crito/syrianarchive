from django.conf.urls import patterns, url
from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^add_announcement', views.add_announcement),
    url(r'^add_link', views.add_link),
)