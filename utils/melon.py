import requests
from bs4 import BeautifulSoup

def get_melon_chart():
    url = "https://www.melon.com/chart/index.htm"
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.39.132 Safari/53.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    song_list = []
    songs = soup.select("#lst50, #lst100")

    for song in songs:
        rank = song.select_one(".rank").get_text(strip=True)
        title = song.select_one(".ellipsis.rank01 a").get_text(strip=True)
        artists = song.select(".ellipsis.rank02 a")
        artist_list = []
        for artist in artists:
            if artist.get_text(strip=True) in artist_list: pass
            else: artist_list.append(artist.get_text(strip=True))
        album = song.select_one(".ellipsis.rank03 a").get_text(strip=True)
        song_list.append({"rank": rank, "title": title, "artists": ', '.join(artist_list), "album":album})

    top_ten_songs = song_list[:5]
    
    return top_ten_songs