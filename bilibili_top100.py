import requests
from bs4 import BeautifulSoup

def get_bilibili_top100():
    url = 'https://www.bilibili.com/v/popular/rank/all'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        video_list = soup.find_all('li', class_='rank-item')

        video_data = []
        for video in video_list[:100]:
            title = video.find('a', class_='title').text.strip()
            author = video.find('a', class_='up-name').text.strip()
            play_count = video.find('span', class_='play').text.strip()
            video_data.append({'title': title, 'author': author, 'play_count': play_count})

        return video_data
    else:
        return None

# 调用函数获取数据
top100_videos = get_bilibili_top100()
if top100_videos:
    for i, video in enumerate(top100_videos, 1):
        print(f"排名：{i}")
        print(f"标题：{video['title']}")
        print(f"作者：{video['author']}")
        print(f"播放量：{video['play_count']}")
        print('---')
else:
    print("Failed to get top 100 videos.")