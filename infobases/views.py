from django.shortcuts import render
from utils.weather import weather_json, pm_json

# Create your views here.

def main(request):
    city_name = request.POST.get('city')
    weather_api = weather_json(city_name)
    pm_api = pm_json(city_name)
    context = {
        'city': weather_api,
        'weather': weather_api['weather'][0]['description'],
        'temp': weather_api['main']['temp'],
        'feels_like': weather_api['main']['feels_like'],
        'temp_min': weather_api['main']['temp_min'],
        'temp_max': weather_api['main']['temp_max'],
        'humidity': weather_api['main']['humidity'],
        'icon': f'https://openweathermap.org/img/wn/{weather_api["weather"][0]["icon"]}@2x.png',
        'PM2_5': pm_api['list'][0]['components']['pm2_5'],
        'PM10': pm_api['list'][0]['components']['pm10']
    }

    if city_name:
        context['selected_city'] = city_name
    return render(request, 'main.html', context)

