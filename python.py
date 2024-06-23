import datetime
import json 
import urllib.request 

weather_data = urllib.request.urlopen('https://api.open-meteo.com/v1/forecast?latitude=32.0479&longitude=-110.712&hourly=temperature_2m,precipitation,snow_depth,visibility,uv_index&temperature_unit=fahrenheit&wind_speed_unit=mph&precipitation_unit=inch&timezone=America%2FDenver&forecast_days=1').read()

data_list = json.loads(weather_data)

hour = datetime.datetime.now().hour

print(hour)
weather = {
        "Temp": str(data_list['hourly']['temperature_2m'][hour]),
        #"Base": str(data_list['snow_depth']['5']),
        #"UV": str(data_list['uv_index'][5]),
        #"Precipitation": str(data_list['precipitation'][5]),
    }

#print(data_list)
print(weather)

#print(data_list.keys())
