from django.shortcuts import render
from utils.weather import weather_json, pm_json

# Create your views here.

def main(request):
    city_name = request.POST.get('city')
    weather_api = weather_json(city_name)
    pm_api = pm_json(city_name)
    pm2_5 = pm_api['list'][0]['components']['pm2_5']
    pm10 = pm_api['list'][0]['components']['pm10']

    # 미세먼지 수치
    if pm2_5 > 75:
        fine_dust = '매우나쁨'
    elif 50 < pm2_5 <= 75:
        fine_dust = '나쁨'
    elif 25 < pm2_5 <= 50:
        fine_dust = '보통'
    elif 10 < pm2_5 <= 25:
        fine_dust = '좋음'
    elif 0 <= pm2_5 <= 10:
        fine_dust = '매우좋음'
    else:
        fine_dust = '확인불가'

    # 초미세먼지 수치
    if pm10 > 200:
        ultrafine_dust = '매우나쁨'
    elif 100 < pm10 <= 200:
        ultrafine_dust = '나쁨'
    elif 50 < pm10 <= 100:
        ultrafine_dust = '보통'
    elif 20 < pm10 <= 50:
        ultrafine_dust = '좋음'
    elif 0 <= pm10 <= 20:
        ultrafine_dust = '매우좋음'
    else:
        ultrafine_dust = '확인불가'
    
    context = {
        'city': weather_api,        # 도시
        'weather': weather_api['weather'][0]['description'],    # 날씨 설명
        'temp': round(weather_api['main']['temp'], 1),                    # 현재 온도
        'feels_like': round(weather_api['main']['feels_like'], 1),        # 체감 온도
        'temp_min': round(weather_api['main']['temp_min'], 1),            # 최고 온도
        'temp_max': round(weather_api['main']['temp_max'], 1),            # 최저 온도
        'humidity': weather_api['main']['humidity'],            # 습도
        'icon': f'https://openweathermap.org/img/wn/{weather_api["weather"][0]["icon"]}@2x.png',    # 날씨 아이콘
        'fine_dust': fine_dust,              # 미세먼지
        'ultrafine_dust': ultrafine_dust,          # 초미세먼지
    }

    if city_name:
        context['selected_city'] = city_name
    return render(request, 'main.html', context)

