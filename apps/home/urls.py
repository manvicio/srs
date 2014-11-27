from django.conf.urls import patterns, include, url
from .views import HomeView, GroupView, ExpertiseView, ContactUsView, CareersView, langView

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^group/$', GroupView.as_view(), name='group'),
    url(r'^expertise/$', 'apps.home.views.ExpertiseView', name='expertise'),
    url(r'^contactus/$', ContactUsView.as_view(), name='contact-us'),
    url(r'^careers/$', CareersView.as_view(), name='careers'),
    url(r'^lang/$', 'apps.home.views.langView', name="lang"),
)
