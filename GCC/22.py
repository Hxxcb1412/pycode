import requests_html
# pprint 可以把数据打印的更整齐
from pprint import pprint
import json
import re
import sqlite3
import pymysql
import matplotlib.pyplot as plt


get_url = 'https://www.shanghairanking.cn/api/pub/v1/bcmr/rank?year=2021&majorCode=080901'
req = requests_html.HTMLSession()
responses = req.get(get_url)
# print(type(responses))
# datas = re.findall('\{(univUp.*?\})\}', responses, re.S)
Sname = re.findall('"univNameCn":"(.*?)"', responses.text)[:15]
Srank = re.findall('"ranking":"(.*?)"', responses.text)[:15]
Sscore = re.findall('"score":(.*?)}', responses.text)[:15]

# re_compair = r'.*univLogo:"(.*)",univNameCn:"(.*)"univNameEn:(.*?),.*univTags:(.*],?),.*univCategory:(.*),province:(.*),score:(.*),ranking:(.*),.*indData:{"411":(.*),"412":(.*),"413":(.*),"414":(.*),"415":(.*),"416":(.*),"417":(.*),"418":(.*),"419":(.*),"420":(.*)}'
# all_datas = []
# for one_data in datas:
#     d_tmp = re.findall(re_compair, one_data, responses.S)
#     all_datas.append(d_tmp[0])
# print(all_datas)


# print(Srank)
# print(Sname)
# print(Sscore)
# pprint(responses.html.html)




# my_dict1 = {k: v for k, v in zip(keys, Srank)}
# for i in range(15):
#     my_dict[keys[0]] = Srank[i]
#     my_dict[keys[1]] = Sname[i]
#     my_dict[keys[2]] = Sscore[i]
#     my_dict.update()

# connection = sqlite3.connect('ranking.db')
# cursor = connection.cursor()
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='ranking',
                     charset='utf8')
cursor = db.cursor()
# 创建表格
cursor.execute("""CREATE TABLE if not exists rank_ing (
    rank int not null,
    university char(20) not null ,
    score float not null
    )charset=utf8;
    """)


#     for row in rows:
#         cells = row.find_all('td')
#         rank = int(cells[0].text.strip())
#         university = cells[1].text.strip()
#         score = float(cells[2].text.strip())


temp_dict = {}
keys = ['rank', 'university', 'score']
for i in range(15):
    # temp_dict[i+1] = {
    # 'rank': int(Srank[i]),
    # 'university': Sname[i],
    # 'score': float(Sscore[i])
    # }

    rank = int(Srank[i])
    university = Sname[i]
    score = float(Sscore[i])
    print(rank, university, score)
    # 插入数据到数据库
    cursor.execute("INSERT INTO rank_ing (rank, university, score) VALUES (%s, %s, %s)", (rank, university, score))

# print(temp_dict)
    # 提交事务并关闭连接
db.commit()
db.close()


con = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='ranking',
                     charset='utf8')
cursor = con.cursor()
# 从数据库中查询数据
cursor.execute("SELECT rank, university, score FROM rank_ing")
data = cursor.fetchall()
# 提取数据
ranks = [row[0] for row in data]
universities = [row[1] for row in data]
scores = [row[2] for row in data]
# 绘制柱状图
plt.bar(universities, scores)
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
plt.xlabel('大学')
plt.ylabel('总分')
plt.title('2021年计算机科学与技术专业排名')
plt.xticks(rotation=30, ha='right')
plt.tight_layout()

# 显示图形
plt.show()
con.close()
