import pymysql
'''
创建桥梁（链接数据库connect）
创建小弟（负责获取数据的cursor）
指示（执行sql命令 execute）
卸货（获取数据fetchall）
关闭（先关闭游标 再关闭链接）
'''
# 1.建立连接
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='python44', charset='utf8')
# 2.创建游标    游标可以记录获取数据的个数
cur = conn.cursor()
# 3.执行sql
sql = "select * from student"
cur.execute(sql)
# 4.获取数据
data = cur.fetchall()
print(data) # 元组类型的 元组中的每一个元素都是一个数据库总的数据
# 5.关闭
cur.close()
conn.close()