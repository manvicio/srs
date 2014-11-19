from django.conf.urls import patterns, include, url
from .views import HomeView, GroupView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^group/$', GroupView.as_view(), name='group'),
)
