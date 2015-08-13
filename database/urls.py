from django.conf.urls import patterns, url
from database import views
from djgeojson.views import GeoJSONLayerView
from database.models import DatabaseEntry

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
    url(r'^collections/$', views.collections, name='collections'),
    url(r'^map_json/$', views.MapLayer.as_view(
        model=DatabaseEntry,
        properties=['popupcontent','violation'],
        ),
      name='incidents'),
    url(r'^map/$', views.map, name='map'),
    url(r'^collection/(?P<id>[0-9]+)/$', views.collection, name='collection'),
	url(r'^(?P<slug>[0-9]+)/$', views.detail, name='detail')
)

