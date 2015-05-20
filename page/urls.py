from django.conf.urls import patterns, url
from page import views

urlpatterns = patterns('',
    url(r'^blog/$', 'page.views.blog', name='blog'),
    url(r'^page/(?P<slug>[\w-]+)/$', 'page.views.page', name='page_detail'),
    url(r'^blog/(?P<slug>[\w-]+)/$', 'page.views.blog_detail', name='blog_detail'),
)