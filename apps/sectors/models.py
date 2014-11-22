from django.db import models

# Create your models here.

class Sector(models.Model):
	nombre_sector = models.CharField(max_length=100)
	descripcion = models.TextField()
