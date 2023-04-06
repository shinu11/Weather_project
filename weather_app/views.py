import requests
from django.http import  HttpResponse
from django.shortcuts import render
from . models import Weather

# Create your views here.

def home(request):
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
    weather_data = Weather.objects.all()


    return render(request,'home.html',{'weather_data':weather_data})