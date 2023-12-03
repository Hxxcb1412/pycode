import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='root',
                     database='ranking',
                     charset='utf8')

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print('success')

db.close()