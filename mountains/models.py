# 3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
# 3300_Project is licensed under a
# Creative Commons Attribution 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <https://creativecommons.org/licenses/by/4.0/>.
from django.db import models

# Create your models here.

class Mountain(models.Model):
  name = models.CharField(max_length=255)
  lat = models.FloatField(null=True)
  lon = models.FloatField(null=True)
