import requests_html
# pprint 可以把数据打印的更整齐
from pprint import pprint
import json
import re
import sqlite3
import pymysql
import matplotlib.pyplot as plt

'''
获取网页内容
'''
get_url = 'https://www.shanghairanking.cn/api/pub/v1/bcmr/rank?year=2021&majorCode=080901'
try:
    req = requests_html.HTMLSession()
    responses = req.get(get_url)
except requests_html.exceptions.RequestException as e:
    print("获取网页内容失败：", e)
# print(type(responses))
# datas = re.findall('\{(univUp.*?\})\}', responses, re.S)

# 提取前15所大学的数据
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

'''
提取数据并保存到数据库
'''
# 创建数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='ranking',
                     charset='utf8')
# 创建游标
cursor = db.cursor()
# 创建表格
cursor.execute("""drop table if exists rank_ing;""")
cursor.execute("""create table if not exists rank_ing (
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


# temp_dict = {}
# keys = ['rank', 'university', 'score']
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
    cursor.execute("insert into rank_ing (rank, university, score) values (%s, %s, %s)", (rank, university, score))
# print(temp_dict)
# 提交事务并关闭连接
db.commit()
db.close()

'''
matplotlib
'''
# 创建数据库连接
con = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='ranking',
                     charset='utf8')
cursor = con.cursor()
# 从数据库中查询数据
cursor.execute("select rank, university, score from rank_ing")  # 返回游标对象，查询语句的结果保存在元组中
data = cursor.fetchall()    # 从查询结果中获取所有数据
# 提取数据
ranks = [row[0] for row in data]
universities = [row[1] for row in data]
scores = [row[2] for row in data]

# 绘制柱状图
bar = plt.bar(universities, scores,
              edgecolor='k',
              linewidth=1)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签 黑体
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
plt.xlabel('中国大学')
plt.ylabel('总分')
plt.title('2021年计算机科学与技术专业排名')
'''
# xticks(ticks=None, labels=None, **kwargs)
#   ticks：x轴刻度位置的列表，若传入空列表，即不显示x轴
#   labels：放在指定刻度位置的标签文本。当ticks参数有输入值，该参数才能传入参数
#   **kwargs：文本属性用来控制标签文本的展示，例如字体大小、字体样式等
'''
plt.xticks(rotation=30, ha='right')     # 旋转30度 旋转方向为右
plt.bar_label(bar)  # 标注数值
plt.tight_layout()  # tight_layout会自动调整子图参数，使之填充整个图像区域

# 显示图形
plt.show()
# 关闭连接
con.close()



'''
plt.bar(x = np.arange(7),        # 横坐标
        height = xiaoming_score, # 柱状高度
        width = 0.35,            # 柱状宽度
        label = '小明',          # 标签
        edgecolor = 'k',         # 边框颜色
        color = 'r',             # 柱状图颜色
        tick_label = subjects,   # 每个柱状图的坐标标签
        linewidth= 3)            # 柱状图边框宽度
plt.legend() #显示标签
plt.show()
'''
