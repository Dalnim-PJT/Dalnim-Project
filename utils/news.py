import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.hada.io/", headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
soup = BeautifulSoup(response.text, 'html.parser')

def news():
    news_dict = {}
    for x in range(0, 5):
        news_dict[soup.select('div.topictitle a')[x]["href"]] = soup.select('div.topictitle h1')[x].text
    return news_dict
