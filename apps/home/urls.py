from django.conf.urls import patterns, include, url
from .views import HomeView, GroupView, ExpertiseView, ContactUsView, CareersView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^group/$', GroupView.as_view(), name='group'),
    url(r'^expertise/$', ExpertiseView.as_view(), name='expertise'),
    url(r'^contactus/$', ContactUsView.as_view(), name='contact-us'),
    url(r'^careers/$', CareersView.as_view(), name='careers'),
)
