from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from apps.projects.models import Proyecto

# Create your views here.

class HomeView(ListView):
	
	template_name = 'index.html'
	model = Proyecto
	context_object_name = 'proyectos'

class GroupView(TemplateView):

	template_name = 'group.html'

class ExpertiseView(TemplateView):

	template_name = 'expertise.html'

class ContactUsView(TemplateView):

	template_name = 'contact-us.html'

class CareersView(TemplateView):

	template_name = 'careers.html'
