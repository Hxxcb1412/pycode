# -*- coding: utf-8 -*-
import requests
from lxml import etree
import csv

def getWeather(url):
    weather_info = []   # 新建一个列表，将爬取的每月数据放进去
    # 请求头信息：浏览器版本型号，接收数据的编码形式

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    # 请求 接收到了相应数据
    resp = requests.get(url, header = headers)
    # 数据预处理
    resp_html = etree.HTML(resp.text)
    # xpath提取所有数据
    resp_list = resp_html.xpath("//ul[@class='weaul']/li]")
    # for循环迭代遍历
    for li in resp_list :
        day_weather_info = {}
        # 日期


weather = []

# for循环生成有顺序的1-12
for month in range (1, 13):
    # 获取某一月的天气信息

    weather_time = '2022' + ('0' + str(month) if month < 10 else str(month))
    print(weather_time)
    url = f''





