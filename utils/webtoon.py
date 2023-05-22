import requests
from bs4 import BeautifulSoup

url = "https://toptoon.com/"
headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.39.132 Safari/53.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
realtime_rank = soup.find("div", {"class": "realtime_rank"})
rank_items = realtime_rank.find_all("li")

def webtoon():
    webtoon_rank = {}
    for rank_item in rank_items:
        rank = rank_item.find("span", {"class": "num"}).text
        title = rank_item.find("span", {"class": "thumb_tit_text"}).text
        view_count = rank_item.find("span", {"class": "viewCountTxt"}).text
        thumbbox_style = rank_item.find("div", {"class": "thumbbox"})["style"]
        image_url = thumbbox_style.split("'")[1]
        link = rank_item.find("a")["href"]
        title_id = link.split("/")[-1]
        # 작품 페이지에 들어가서 작가 정보 추출
        info_url = f"https://toptoon.com/comic/ep_list/{title_id}"
        response = requests.get(info_url)
        soup = BeautifulSoup(response.text, "html.parser")
        author = soup.find("span", {"class": "comic_wt"}).text
        webtoon_rank[rank] = [image_url, title, author, view_count, info_url]
    return webtoon_rank

    # print(f"{rank}. {title} ({view_count}), 작가: {author}, 이미지 URL: {image_url}")