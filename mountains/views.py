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
from .models import Mountain

def mountains(response):
    mymountains = Mountain.objects.all().order_by('name').values('name', 'pass_type')
    return render(response, "mountains/mountains.html", {'mymountains': mymountains})

def forecast(response, name):
    mymountain = Mountain.objects.get(name=name)
    lat = mymountain.lat
    lon = mymountain.lon

    weather_url = (
        f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}'
        '&current=temperature_2m,precipitation&hourly=snow_depth,visibility,uv_index&daily=temperature_2m_max,precipitation_sum'
        '&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=3'
    )
   
    weather_data = urllib.request.urlopen(weather_url).read()
    data_list = json.loads(weather_data)
   
    current_hour = datetime.datetime.now().hour

    Temp = str(data_list['current']['temperature_2m'])
    Precipitation = str(data_list['current']['precipitation'])
    Visibility = str(data_list['hourly']['visibility'][current_hour])
    Base = str(data_list['hourly']['snow_depth'][current_hour])
    UV = str(data_list['hourly']['uv_index'][current_hour])

    Temp24 = str(data_list['daily']['temperature_2m_max'][1])
    Precip24 = str(data_list['daily']['precipitation_sum'][1])
    
 
    context = {
        'mymountain': mymountain,
        'Temp': Temp,
        'UV': UV,
        'Visibility': Visibility,
        'Base': Base,
        'Precipitation': Precipitation,
        'resort_url': mymountain.resort_url,
        'background_image_url': mymountain.background_image.url if mymountain.background_image else None,
        'Temp24' : Temp24,
        'Precip24' : Precip24,
   }
 
    return render(response, "mountains/forecast.html", context)
