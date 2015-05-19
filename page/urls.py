from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',
    url(r'^(?P<slug>[\w-]+)/$', 'page.views.page', name='page_detail'),
)