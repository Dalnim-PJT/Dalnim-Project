import requests
from bs4 import BeautifulSoup

url = 'https://www.cgv.co.kr'
response = requests.get(url)
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
