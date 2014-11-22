from django.conf.urls import patterns, include, url
from .views import ServicesView

urlpatterns = patterns('',
    url(r'^$', ServicesView.as_view(), name='services'),
)