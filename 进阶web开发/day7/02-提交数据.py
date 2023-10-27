import pymysql

# 1.建立连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='python44', charset='utf8')

# 2.创建游标    游标可以记录获取数据的个数
cur = conn.cursor()

# 3.执行sql
sql = "update student set age=22 where name='shido'"
cur.execute(sql)

# 4.获取数据
# 元组类型的 元组中的每一个元素都是一个数据库总的数据
sql = "select * from student"
cur.execute(sql)
data = cur.fetchall()
for i in data:
    print(i)

# 只要对数据库中的数据进行修改    就需要进行提交操作 否则不会真正的修改
conn.commit()

# 5.关闭
cur.close()
conn.close()
