from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^me/$', views.me, name='me'),
	url(r'^login/$', views.loginuser, name='login'),
	url(r'^logout/$', views.logoutuser, name='logout'),
	url(r'^account/$', 'account'),
    url(r'^edit/$', views.edit_account, name='edit'),
    url(r'^me/edit/$', views.me_edit_account, name='edit'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<profile_id>\d+)/$', views.detail, name='detail'),
    #password resets
    url(r'^password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/'},name="password_reset"),
    url(r'^password/reset/done/$','django.contrib.auth.views.password_reset_done'),
    url(r'^password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
    url(r'^password/done/$', 'django.contrib.auth.views.password_reset_complete'),
)
