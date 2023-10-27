
# 导入数据请求模块
import requests
# 导入数据解析模块
import parsel
# 导入csv模块
import csv
# 创建csv文件
f = open('热搜.csv', mode='a', encoding='utf-8', newline='')
# 配置文件
csv_writer = csv.DictWriter(f, fieldnames=['排名', '标题', '热度'])
# 写入表头
csv_writer.writeheader()

# 确定请求网址
url = 'https://s.weibo.com/top/summary?cate=realtimehot'
# 请求头伪装
headers = {
    # cookie    用户信息，常用于检测是否有登录账号
    'cookie': 'SUB=_2AkMSWLRjf8NxqwJRmfsUyGLgb4RzyQzEieKkBEW4JRMxHRl-yT8XqmAhtRB6OdiajHjnF1OPT1t0pa6gGlG8lItpZrJy; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF-QMoTypbRaqmJjmy61UCa; b-user-id=e2c4863a-3c79-be36-666e-730e9872096e; _s_tentry=-; Apache=7715065731456.341.1697728355934; SINAGLOBAL=7715065731456.341.1697728355934; ULV=1697728355991:1:1:1:7715065731456.341.1697728355934:',
    # user-agent    用户代理 表示浏览器基本身份标识
    'user-agent': 'SUB=_2AkMSWLRjf8NxqwJRmfsUyGLgb4RzyQzEieKkBEW4JRMxHRl-yT8XqmAhtRB6OdiajHjnF1OPT1t0pa6gGlG8lItpZrJy; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF-QMoTypbRaqmJjmy61UCa; b-user-id=e2c4863a-3c79-be36-666e-730e9872096e; _s_tentry=-; Apache=7715065731456.341.1697728355934; SINAGLOBAL=7715065731456.341.1697728355934; ULV=1697728355991:1:1:1:7715065731456.341.1697728355934:'
}
# 发送请求
response = requests.get(url=url, headers=headers)
# 获取相应的文本数据
print(response.text)

# 转数据类型
selector = parsel.Selector(response.text)
# 第一次提取 css选择器 获取所有标签数据内容
trs = selector.css(('#pl_top_realtimehot tbody tr'))

num = 1
# for 循环遍历
for tr in trs:
    # 获取热搜标题
    title = tr.css('.td-02 a::text').get()
    # 获取热搜热度
    hot = tr.css('.td-02 span::text').get()
    # 创建字典保存数据
    dit = {
        '排名': num,
        '标题': title,
        '热度': hot
    }
    # 保存数据
    csv_writer.writerow(dit)
    print(dit)
    num += 1
