# 3300_Project
# (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
# This file is part of the 3300_Project and is licensed under the GNU Affero General Public License (AGPLv3).
# You may obtain a copy of the AGPLv3 license at <https://www.gnu.org/licenses/agpl-3.0.en.html>.
#
# This project uses weather data from Open-Meteo (<https://open-meteo.com/>),
# licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
# You can view the license at <https://creativecommons.org/licenses/by/4.0/>.
from django.db import models

# Create your models here.

class Mountain(models.Model):
  name = models.CharField(max_length=255)
  lat = models.FloatField(null=True)
  lon = models.FloatField(null=True)
  pass_type = models.CharField(max_length=10, choices=[('epic', 'Epic Pass'), ('ikon', 'Ikon Pass'), ('other', 'Other')], default='unknown')
  resort_url = models.URLField(max_length=200, blank=True)
  background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
