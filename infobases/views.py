from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from utils.weather import weather_json, pm_json
from utils.news import news
from utils.youtube import youtube_trending_video
from utils.melon import get_melon_chart
from utils.books import books
from utils.movie import movie
from utils.webtoon import webtoon
from .models import Info, Image, Comment
from .forms import InfoForm, CommentForm, ImageForm
from django.db.models.signals import pre_save
from django.dispatch import receiver


# Create your views here.

def main(request):
    infos = Info.objects.all()
    city_name = request.GET.get('city', 'Seoul')
    books_category = request.GET.get('books', '001')
    weather_api = weather_json(city_name)
    pm_api = pm_json(city_name)
    pm2_5 = pm_api['list'][0]['components']['pm2_5']
    pm10 = pm_api['list'][0]['components']['pm10']
    news_dict = news()
    books_list = books(books_category)
    youtube_trending_video_list = youtube_trending_video()
    top_ten_songs = get_melon_chart()
    movies = movie()
    webtoons = webtoon()
    cities = [ {'name': '서울', 'value': 'Seoul'}, {'name': '부산', 'value': 'Busan'}, {'name': '대구', 'value': 'Daegu'}, {'name': ' 대전', 'value': 'Daejeon'}, {'name': '광주', 'value': 'Gwangju'}, {'name': '인천', 'value': 'Incheon'}, {'name': '제주', 'value': 'Jeju' }, {'name': '런던', 'value': 'london'}, {'name': '베이징', 'value': 'beijing'}, {'name': '도쿄', 'value': 'tokyo'}, {'name': '방콕' , 'value': 'bangkok'}, {'name': '시드니', 'value': 'sydney'}, {'name': '토론토', 'value': 'toronto'}, {'name': '뉴욕', 'value': 'new york'} , {'name': '암스테르담', 'value': 'Amsterdam'}, {'name': '베를린', 'value': 'Berlin'}, {'name': '부다페스트', 'value': 'Budapest'}, {'name': '카이로', 'value': 'Cairo'}, {'name': '캔버라', 'value': 'Canberra'}, {'name': '두바이', 'value': 'Dubai'}, {'name': '로마', 'value': 'Rome'}, { 'name': '싱가폴', 'value': 'Singapore'}, {'name': '파리', 'value': 'Paris'}, {'name': '마닐라', 'value': 'Manila'}, {'name': '홍콩', 'value': 'Hong Kong'}, {'name': '하노이', 'value': 'Hanoi'}]

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
        'icon': f"https://openweathermap.org/img/wn/{weather_api['weather'][0]['icon']}@2x.png",    # 날씨 아이콘
        'fine_dust': fine_dust,              # 미세먼지
        'ultrafine_dust': ultrafine_dust,          # 초미세먼지
        'news_dict': news_dict,
        'cities': cities,
        'youtube_trending_video_list': youtube_trending_video_list,
        'top_ten_songs': top_ten_songs,
        'books_list': books_list,
        'movies' : movies,
        'webtoons' : webtoons,
        'infos': infos,
    }

    if city_name:
        context['selected_city'] = city_name
    if books_category:
        context['selected_book'] = books_category
    return render(request, 'infobases/main.html', context)


@login_required
def create(request):
    info_form = InfoForm()
    image_form = ImageForm()
    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        files = request.FILES.getlist('image')
        if info_form.is_valid():
            form = info_form.save(commit=False)
            form.user = request.user
            form.save()
            for i in files:
                Image.objects.create(image=i, info=form)
            return redirect('infobases:detail', form.pk)
    context = {
        'info_form': info_form,
        'image_form': image_form,
    }
    return render(request, 'infobases/create.html', context)


def detail(request, infobase_pk):
    info = Info.objects.get(pk=infobase_pk)
    comments = info.comment_set.all()
    comment_form = CommentForm()
    form = CommentForm(request.POST, instance=info)
    info.views += 1
    info.save()
    
    info_images = []
    images = Image.objects.filter(info=info)
    if images:
        info_images.append((info, images))
    else:
        info_images.append((info, ''))
    
    context = {
        'info': info,
        'info_images': info_images,
        'comments': comments,
        'comment_form': comment_form,
        'form': form,
    }
    return render(request, 'infobases/detail.html', context)


@login_required
def delete(request, infobase_pk):
    info = Info.objects.get(pk=infobase_pk)
    if info.user == request.user:
        info.delete()
    return redirect('infobases:main')


@login_required
def update(request, infobase_pk):
    info = Info.objects.get(pk=infobase_pk)
    if request.user == info.user:
        if request.method == 'POST':
            info_form = InfoForm(request.POST, instance=info)
            files = request.FILES.getlist('image')
            if form.is_valid():
                form = info_form.save(commit=False)
                form.user = request.user
                form.save()
                for i in files:
                    Image.objects.create(image=i, product=form)
                return redirect('infobases:detail', form.pk)
        else:
            info_form = InfoForm(instance=info)
            image_form = ImageForm()
    else:
        return redirect('infobases:main')
    context = {
        'info': info,
        'info_form': info_form,
        'image_form': image_form,
    }
    return render(request, 'infobases/update.html', context)


@login_required
def comments_create(request, infobase_pk):
    info = Info.objects.get(pk=infobase_pk)
    comment_form = CommentForm(request.POST)
    
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.info = info
        comment.user = request.user
        comment = comment_form.save()
        return redirect('infobases:detail', info.pk)
    context = {
        'info': info,
        'comment_form': comment_form,
    }
    return render(request, 'infobases/detail.html', context)


@login_required
def comments_delete(request, infobase_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('infobases:detail', infobase_pk)


@receiver(pre_save, sender=Info)
def increment_view_count(sender, instance, **kwargs):
    if instance.pk is None:
        return
    old_instance = Info.objects.get(pk=instance.pk)
    if old_instance.views != instance.views:
        instance.views = old_instance.views + 1

