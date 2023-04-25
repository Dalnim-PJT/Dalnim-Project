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
        img_url = song.select_one('.image_typeAll img')['src']
        album_url = song.select_one(".ellipsis.rank03 a")['href']
        res_album_url = ''.join([num for num in album_url if num.isdigit()])
        music_url = "https://www.melon.com/album/detail.htm?albumId=" + res_album_url
        song_list.append({"rank": rank, "title": title, "artists": ', '.join(artist_list), "album": album, "image": img_url, "music_url": music_url,})

# url을 두개를 사용해야 하는데 예상 문제는 header를 적용하지 않아서 차단돼서 url이 안가져와지나..? 하는 생각...
    top_ten_songs = song_list[:10]
    
    return top_ten_songs