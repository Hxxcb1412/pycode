import requests
from bs4 import BeautifulSoup

def get_huolongguo_shuodian_up_video_titles():
    url = 'https://space.bilibili.com/270741154/video'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        video_list = soup.find_all('li', class_='video-item matrix')

        video_titles = []
        for video in video_list:
            title = video.find('a', class_='title')['title']
            video_titles.append(title)

        return video_titles
    else:
        return None

# 调用函数获取数据
video_titles = get_huolongguo_shuodian_up_video_titles()
if video_titles:
    for title in video_titles:
        print(title)
else:
    print("Failed to get video titles.")