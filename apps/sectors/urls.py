from django.conf.urls import patterns, url
from .views import SectorDetalleView


urlpatterns = patterns('',

	url(r'^(?P<slug>[-\w]+)/$', SectorDetalleView.as_view(), name='sector_detalle'),
)