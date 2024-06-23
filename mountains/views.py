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
    #Base = str(data_list['hourly']['snow_depth'][hour])
    UV = str(data_list['hourly']['uv_index'][hour])
    Visibility = str(data_list['hourly']['visibility'][hour])
    Precipitation = str(data_list['hourly']['precipitation'][hour])
    
    #print(weather)
    return render(response, "mountains/forecast.html", {'mymountain':mymountain, 'Temp':Temp,
    'UV':UV, 'Visibility':Visibility, 'Precipitation':Precipitation})
