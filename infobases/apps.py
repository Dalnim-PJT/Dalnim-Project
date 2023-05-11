from django.apps import AppConfig
from utils.youtube import youtube_trending_video
from utils.news import news
from utils.melon import get_melon_chart
from utils.movie import movie
from utils.webtoon import webtoon
from utils.books import books


class InfobasesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'infobases'

    global youtube_trending_video_list, news_dict, top_ten_songs, movies, webtoons, books_list
    youtube_trending_video_list = youtube_trending_video()
    news_dict = news()
    top_ten_songs = get_melon_chart()
    movies = movie()
    webtoons = webtoon()
    books_list = books('001')

