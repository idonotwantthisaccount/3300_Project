#3300_Project (c) by Brian Richardson, Ethan Briggs, Jordan Camden, and Thomas Gherna
#
#3300_Project is licensed under a
#Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.
#
#You should have received a copy of the license along with this
#work. If not, see <https://creativecommons.org/licenses/by-nc-sa/4.0/>.
import datetime
import json 
import urllib.request 

weather_data = urllib.request.urlopen('https://api.open-meteo.com/v1/forecast?latitude=32.0479&longitude=-110.712&hourly=temperature_2m,precipitation,snow_depth,visibility,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1').read()

data_list = json.loads(weather_data)

hour = datetime.datetime.now().hour

print(hour)
    
Temp = str(data_list['hourly']['temperature_2m']) + 'F'
#Base = str(data_list['hourly']['snow_depth'][hour])
UV = str(data_list['hourly']['uv_index'][hour])
Visibility = str(data_list['hourly']['visibility'][hour])
Precipitation = str(data_list['hourly']['precipitation'][hour])

#print(data_list)
print(Temp)
print(UV)
print(Visibility)
print(Precipitation)

#print(data_list.keys())
