# 3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
# 3300_Project is licensed under a
# Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#
# You should have received a copy of the license along with this
# work. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
from django.shortcuts import render
import json, datetime
import urllib.request


# Create your views here.

from django.shortcuts import render
from .models import Mountain

def mountains(response):
    mymountains = Mountain.objects.all().values()
    context = { 'mymountains' : mymountains, }
    return render(response, "mountains/mountains.html", {'mymountains' : mymountains})

def forecast(response, name):
    mymountain = Mountain.objects.get(name=name)
    lat = mymountain.lat
    lon = mymountain.lon

    weather_data = urllib.request.urlopen(
        'https://api.open-meteo.com/v1/forecast?latitude=' + str(lat) + '&longitude=' + str(lon) + 
             '&current=temperature_2m&hourly=precipitation,visibility,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1').read()
    
    data_list = json.loads(weather_data)
    
    hour = datetime.datetime.now().hour


    Temp = str(data_list['current']['temperature_2m']) + 'F'
    Precipitation = str(data_list['hourly']['precipitation'][hour])
    Visibility = str(data_list['hourly']['visibility'][hour])
    #Base = str(data_list['hourly']['snow_depth'][hour])
    UV = str(data_list['hourly']['uv_index'][hour])
    
    #print(weather)
    return render(response, "mountains/forecast.html", {'mymountain':mymountain, 'Temp':Temp,
    'UV':UV, 'Visibility':Visibility, 'Precipitation':Precipitation, 'hour':hour})
