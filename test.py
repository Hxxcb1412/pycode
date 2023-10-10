import requests
from bs4 import BeautifulSoup
def test():
    url = "https://space.bilibili.com/40665101/video"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0'}
    res = requests.get(url, headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'html.parser')
        video_list = soup.find_all('li', class_='small-item fakeDanmu-item')

        video_titles = []
        for video in video_list:
            title = video.find('a', class_="title")['title']
            video_titles.append(title)

        return video_titles
    else:
        return None

video_titles = test()
if video_titles:
    for title in video_titles:
        print(title)

    else:
        print("failed")