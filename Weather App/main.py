import requests
import json
 
api_key = "cdf4e0970b394e0199564724231609"
city = input("Enter the name of city: ")
url = f"http://api.weatherapi.com/v1/current.json?key=cdf4e0970b394e0199564724231609 &q={city}" 

r = requests.get(url)
# print(r.text)
weather_dic = json.loads(r.text)
print("Region : " +  weather_dic["location"]["region"])
print("Country : " +  weather_dic["location"]["country"])
print("Localtime : " +  weather_dic["location"]["localtime"])
print("Temp in Celcius : " +  str(weather_dic["current"]["temp_c"]))
print("Temp in Fahrenhite : " +  str(weather_dic["current"]["temp_f"]))
if(weather_dic["current"]["is_day"]=="1"):
    print(f"Its night in {city}")
else:
    print(f"Its day in {city}")
if "wind_kph" in weather_dic:
    wind_kph = weather_dic["wind_kph"]
    print("Wind Speed in mph:", wind_kph)
else:
    print("Wind speed information not found")
if "wind_dir" in weather_dic:
    wind_dir = weather_dic["wind_dir"]
    print("Wind Direction:", wind_dir)
else:
    print("Wind Direction information not found")
if "humidity" in weather_dic:
    humidity = weather_dic["humidity"]
    print("Wind Direction:", humidity)
else:
    print("Humidity information not found")
