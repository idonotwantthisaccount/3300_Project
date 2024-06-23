from django.db import models

# Create your models here.

class Mountain(models.Model):
  name = models.CharField(max_length=255)
  lat = models.FloatField(null=True)
  lon = models.FloatField(null=True)
