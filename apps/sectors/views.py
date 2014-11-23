from django.shortcuts import render
from django.views.generic import DetailView
from .models import Sector

# Create your views here.

class SectorDetalleView(DetailView):
	template_name = "sector_detalle.html"
	model = Sector
