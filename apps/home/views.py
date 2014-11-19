from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
	
	template_name = 'index.html'

class GroupView(TemplateView):

	template_name = 'group.html'

class ExpertiseView(TemplateView):

	template_name = 'expertise.html'

class ContactUsView(TemplateView):

	template_name = 'contact-us.html'

class CareersView(TemplateView):

	template_name = 'careers.html'
