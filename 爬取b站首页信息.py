import requests

def get_bilibili_homepage_data():
    url = 'https://www.bilibili.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        return None

# 调用函数获取数据
homepage_data = get_bilibili_homepage_data()
if homepage_data:
    print(homepage_data)
else:
    print("Failed to get homepage data.")