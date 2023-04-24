import requests
from bs4 import BeautifulSoup
import ssl
from time import sleep

# url = 'https://www.cgv.co.kr'
url = 'https://www.megabox.co.kr'
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.39.132 Safari/53.36'}
response = requests.get(url, verify=False, headers=headers, timeout=30)
soup = BeautifulSoup(response.text, 'html.parser')
movies = soup.select('div.swiper-wrapper > div.swiper-slide.swiper-slide-movie')
def movie():
    rank = 1
    movie_list = {}
    for movie in movies:
        img_url = movie.select_one('.img_wrap > img')['src']
        title = movie.select_one('.movie_info_wrap > strong').text
        egg = movie.select_one('.movie_info_wrap > span > img')['src']
        rating = movie.select_one('.movie_info_wrap > span').text
        ticketing = movie.select_one('.movie_info_wrap > span:nth-child(3)').text
        info_url = url + movie.select_one('.img_wrap > .movieChart_btn_wrap > a.btn_movieChart_detail')['href']
        ticketing_url = url + movie.select_one('.img_wrap > .movieChart_btn_wrap > a.btn_movieChart_ticketing')['href']
        movie_list[rank] = [img_url, title, egg, rating, ticketing, info_url, ticketing_url]
        rank += 1
        if rank == 11:
            break
    return movie_list
