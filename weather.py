import requests
from datetime import datetime

api_key = '4be13bff94732a66cb8ff8fcaadc6162'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')
str0 = str(location)
str1 = str(date_time)
str2 = str(temp_city)
str3 = str(hmdt)
str4 = str(weather_desc)
str5 = str(wind_spd)
L = [str0, "\t", str1, "\t", str2, "\t", str3,"\t", str4,"\t", str5]
with open('Mausam.txt','a') as file:
 file.writelines(L)
 file.write("\n")