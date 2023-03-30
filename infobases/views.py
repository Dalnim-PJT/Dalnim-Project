from django.shortcuts import render
from utils.weather import weather_json

# Create your views here.

def main(request):
    city_name = request.POST.get('city')
    city = weather_json(city_name)
    context = {
        'city': city,
        'weather': city['weather'][0]['description'],
        'temp': city['main']['temp'],
        'feels_like': city['main']['feels_like'],
        'temp_min': city['main']['temp_min'],
        'temp_max': city['main']['temp_max'],
        'humidity': city['main']['humidity'],
        'icon': f'https://openweathermap.org/img/wn/{city["weather"][0]["icon"]}@2x.png',
    }

    if city_name:
        context['selected_city'] = city_name
    return render(request, 'main.html', context)

