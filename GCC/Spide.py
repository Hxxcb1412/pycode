import requests
from bs4 import BeautifulSoup
import sqlite3
import matplotlib.pyplot as plt

# 获取网页内容
def get_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("获取网页内容失败：", e)
        return None

# 提取数据并保存到数据库
def extract_data(html):
    # 创建数据库连接
    connection = sqlite3.connect('ranking.db')
    cursor = connection.cursor()

    # 创建表格
    cursor.execute('''CREATE TABLE IF NOT EXISTS ranking (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        rank INTEGER NOT NULL,
        university TEXT NOT NULL,
        score REAL NOT NULL
    )''')

    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(html, 'html.parser')

    # 提取前15所大学的数据
    table = soup.find('div', class_='univ-detail')
    rows = table.tbody.find_all('a')[:15]

    for row in rows:
        cells = row.find_all('td')
        rank = int(cells[0].text.strip())
        university = cells[1].text.strip()
        score = float(cells[2].text.strip())

        # 插入数据到数据库
        cursor.execute("INSERT INTO ranking (rank, university, score) VALUES (?, ?, ?)", (rank, university, score))

    # 提交事务并关闭连接
    connection.commit()
    connection.close()

# 数据可视化
def plot_data():
    # 创建数据库连接
    connection = sqlite3.connect('ranking.db')
    cursor = connection.cursor()

    # 从数据库中查询数据
    cursor.execute("SELECT rank, university, score FROM ranking")
    data = cursor.fetchall()

    # 提取数据
    ranks = [row[0] for row in data]
    universities = [row[1] for row in data]
    scores = [row[2] for row in data]

    # 绘制柱状图
    plt.bar(universities, scores)
    plt.xlabel('大学')
    plt.ylabel('总分')
    plt.title('2021年计算机科学与技术专业排名')
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()

    # 显示图形
    plt.show()

    # 关闭连接
    connection.close()

if __name__ == '__main__':
    url = 'https://www.shanghairanking.cn/rankings/bcmr/2021/080901'
    html = get_page(url)
    if html:
        extract_data(html)
        plot_data()
