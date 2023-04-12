import requests
import random

def youtube_trending_video():
    region_code = 'KR'
    max_results = 5
    youtube_trending_video_list = []
    url = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode={region_code}&maxResults={max_results}&key={apikey}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        for video in data['items']:
            # title = video['snippet']['title']
            # channel = video['snippet']['channelTitle']
            video_id = video['id']
            video_link = f'https://www.youtube.com/embed/{video_id}?&autoplay=0&mute=1'
            youtube_trending_video_list.append(video_link)
    else:
        print('API 요청 실패')
    
    return random.choice(youtube_trending_video_list)


with open('etc/youtube_apikey.txt') as f:
    apikey = f.read().strip()