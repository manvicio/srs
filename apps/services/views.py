from django.shortcuts import render_to_response
from django.views.generic import TemplateView
from django.template import RequestContext
from apps.sectors.models import Sector
from apps.services.models import Servicio

# Create your views here.
class ServicesView(TemplateView):
	
	template_name = "services.html"

def ServicesView(request):
	sectores = Sector.objects.all()
	servicios = Servicio.objects.all()
	return render_to_response('services.html',{'sectores': sectores,'servicios':servicios}, context_instance=RequestContext(request))