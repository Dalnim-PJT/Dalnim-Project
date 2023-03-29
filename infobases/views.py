from django.shortcuts import render
from utils.weather import weather_json

# Create your views here.

def main(request):
    seoul = weather_json('seoul')

    context = {
        'seoul': seoul,
        'weather': seoul['weather'][0]['description'],
        'temp': seoul['main']['temp'],
        'feels_like': seoul['main']['feels_like'],
        'temp_min': seoul['main']['temp_min'],
        'temp_max': seoul['main']['temp_max'],
        'humidity': seoul['main']['humidity'],
    }
    return render(request, 'main.html', context)

