import requests
import re
import sqlite3
import matplotlib.pyplot as plt

import re
import requests


url = 'https://www.shanghairanking.cn/rankings/bcmr/2021/080901'
re = requests.get(url, timeout=20)
# if r.status_code == 200:
#     r.encoding = 'utf-8'

datas = re.findall('\{(univUp.*?\})\}',js_str,re.S)
re_compair = r'.*univLogo:"(.*)",univNameCn:"(.*)",univNameEn:(.*?),.*univTags:(.*],?),.*univCategory:(.*),province:(.*),score:(.*),ranking:(.*?),.*indData:{"411":(.*),"412":(.*),"413":(.*),"414":(.*),"415":(.*),"416":(.*),"417":(.*),"418":(.*),"419":(.*),"420":(.*)}'
all_datas = []
for one_data in datas:
    d_tmp = re.findall(re_compair,one_data,re.S)
    all_datas.append(d_tmp[0])


# # 获取网页内容
# def get_page(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#         return response.text
#     except requests.exceptions.RequestException as e:
#         print("获取网页内容失败：", e)
#         return None
#
# # 提取数据并保存到数据库
# def extract_data(html):
#     # 使用正则表达式提取排名、学校名称和总分
#     pattern = r'<tr>.*?<td>(\d+)</td>.*?<a data-toggle="tooltip".*?>(.*?)</a>.*?<td class="align-middle">(\d+\.\d+)</td>.*?</tr>'
#     results = re.findall(pattern, html, re.DOTALL)
#
#     # 创建数据库连接
#     connection = sqlite3.connect('ranking.db')
#     cursor = connection.cursor()
#
#     # 创建表格
#     cursor.execute('''CREATE TABLE IF NOT EXISTS ranking (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         rank INTEGER NOT NULL,
#         university TEXT NOT NULL,
#         score REAL NOT NULL
#     )''')
#
#     # 插入数据到数据库
#     for result in results[:15]:
#         rank, university, score = result
#         cursor.execute("INSERT INTO ranking (rank, university, score) VALUES (?, ?, ?)", (int(rank), university, float(score)))
#
#     # 提交事务并关闭连接
#     connection.commit()
#     connection.close()
#
# # 数据可视化
# def plot_data():
#     # 创建数据库连接
#     connection = sqlite3.connect('ranking.db')
#     cursor = connection.cursor()
#
#     # 从数据库中查询数据
#     cursor.execute("SELECT university, score FROM ranking ORDER BY id LIMIT 15")
#     data = cursor.fetchall()
#
#     # 提取数据
#     universities = [row[0] for row in data]
#     scores = [row[1] for row in data]
#
#     # 绘制柱状图
#     plt.bar(universities, scores)
#     plt.xlabel('大学')
#     plt.ylabel('总分')
#     plt.title('2021年计算机科学与技术专业前15所大学排名')
#     plt.xticks(rotation=30, ha='right')
#     plt.tight_layout()
#
#     # 显示图形
#     plt.show()
#
#     # 关闭连接
#     connection.close()
#
# if __name__ == '__main__':
#     url = 'https://www.shanghairanking.cn/rankings/bcmr/2021/080901'
#     html = get_page(url)
#     if html:
#         extract_data(html)
#         plot_data()
