from django.shortcuts import render_to_response
from django.views.generic import TemplateView, ListView
from django.template import RequestContext
from apps.projects.models import Proyecto
from apps.team.models import Miembro
from .models import TextoServicios, TextoProyectos
from django.utils.translation import ugettext as _
from django.http import HttpResponse

# Create your views here.

class HomeView(ListView):
	
	template_name = 'index.html'
	model = Proyecto
	context_object_name = 'proyectos'

class GroupView(ListView):

	template_name = 'group.html'
	model = Miembro
	context_object_name = 'miembros'

def ExpertiseView(request):
	text_services = TextoServicios.objects.all()
	text_projects = TextoProyectos.objects.all()
	projects = Proyecto.objects.all()
	return render_to_response('expertise.html',{'text_services': text_services,'text_projects':text_projects, 'projects': projects}, context_instance=RequestContext(request))

class ContactUsView(TemplateView):

	template_name = 'contact-us.html'

class CareersView(TemplateView):

	template_name = 'careers.html'

def langView(request):
	salida = _("Welcome to my site")
	return HttpResponse(salida)
