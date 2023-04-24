import requests
from bs4 import BeautifulSoup

def books(category):
    response = requests.get(f'http://www.yes24.com/24/category/bestseller?CategoryNumber={category}&sumgb=06', headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
    soup = BeautifulSoup(response.text, 'html.parser')
    books_dict = []
    for x in range(5):
        temp_dict = {}
        temp_dict['book_rank'] = x+1
        temp_dict['book_name'] = soup.select('td.goodsTxtInfo')[x].select('a')[0].text
        temp_dict['book_author'] = ' '.join(soup.select('td.goodsTxtInfo > div.aupu')[x].text.split())
        temp_dict['book_link'] = 'http://www.yes24.com' + soup.select('td.goodsTxtInfo')[x].select('a')[0]['href']
        temp_dict['book_img_link'] = soup.select('div.goodsImgW')[x].select('a > img')[0]['src']
        books_dict.append(temp_dict)
    return books_dict
