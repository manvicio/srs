from django.conf.urls import patterns, include, url
from .views import HomeView, GroupView, ExpertiseView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^group/$', GroupView.as_view(), name='group'),
    url(r'^expertise/$', ExpertiseView.as_view(), name='expertise'),
)
