# 3300_Project
# (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
# This file is part of the 3300_Project and is licensed under the GNU Affero General Public License (AGPLv3).
# You may obtain a copy of the AGPLv3 license at <https://www.gnu.org/licenses/agpl-3.0.en.html>.
#
# This project uses weather data from Open-Meteo (<https://open-meteo.com/>),
# licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).
# You can view the license at <https://creativecommons.org/licenses/by/4.0/>.
from django.shortcuts import render
import json, datetime
import urllib.request


# Create your views here.

from django.shortcuts import render
from .models import Mountain

def mountains(response):
    mymountains = Mountain.objects.all().order_by('name').values('name', 'pass_type')
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
    'UV':UV, 'Visibility':Visibility, 'Precipitation':Precipitation})
