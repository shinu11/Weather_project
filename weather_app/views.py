import requests
from django.http import  JsonResponse
from django.shortcuts import render
from . models import Weather
import datetime
# Create your views here.

def home(request,firstRequest=0):
    api_key = "f248c9509875d37a30bd011301a08928"
    city = "kerala"
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    location = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    Weather.objects.create(location=location,temperature=temperature,humidity=humidity,wind_speed=wind_speed)
    weather_data = Weather.objects.last()
    weather_res = {
        "location":weather_data.location,
        "temperature":weather_data.temperature,
        "humidity":weather_data.humidity,
        "wind_speed":weather_data.wind_speed,
        "time_now":datetime.datetime.now()
    }
    if(firstRequest==1):
        return JsonResponse(weather_res)
    return render(request,'home.html',{"weather_data":weather_res})