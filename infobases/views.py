from django.shortcuts import render
from utils.weather import weather_json, pm_json
from utils.news import news
from utils.youtube import youtube_trending_video

# Create your views here.

def main(request):
    city_name = request.POST.get('city')
    weather_api = weather_json(city_name)
    pm_api = pm_json(city_name)
    pm2_5 = pm_api['list'][0]['components']['pm2_5']
    pm10 = pm_api['list'][0]['components']['pm10']
    news_dict = news()
    youtube_trending_video_list = youtube_trending_video()
    cities = [ {"name": "서울", "value": "Seoul"}, {"name": "부산", "value": "Busan"}, {"name": "대구", "value": "Daegu"}, {"name": " 대전", "value": "Daejeon"}, {"name": "광주", "value": "Gwangju"}, {"name": "인천", "value": "Incheon"}, {"name": "제주", "value": "Jeju" }, {"name": "런던", "value": "london"}, {"name": "베이징", "value": "beijing"}, {"name": "도쿄", "value": "tokyo"}, {"name": "방콕" , "value": "bangkok"}, {"name": "시드니", "value": "sydney"}, {"name": "토론토", "value": "toronto"}, {"name": "뉴욕", "value": "new york"} , {"name": "암스테르담", "value": "Amsterdam"}, {"name": "베를린", "value": "Berlin"}, {"name": "부다페스트", "value": "Budapest"}, {"name": "카이로", "value": "Cairo"}, {"name": "캔버라", "value": "Canberra"}, {"name": "두바이", "value": "Dubai"}, {"name": "로마", "value": "Rome"}, { "name": "싱가폴", "value": "Singapore"}, {"name": "파리", "value": "Paris"}, {"name": "마닐라", "value": "Manila"}, {"name": "홍콩", "value": "Hong Kong"}, {"name": "하노이", "value": "Hanoi"}]

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
        'news_dict': news_dict,
        'cities': cities,
        'youtube_trending_video_list': youtube_trending_video_list,
    }

    if city_name:
        context['selected_city'] = city_name
    return render(request, 'main.html', context)

    