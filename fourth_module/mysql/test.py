# -*- coding: utf-8 -*-

# __title__ = 'test.py'
# __author__ = 'yangyang'
# __mtime__ = '2018.03.26'




import pymysql

conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
cursor = conn.cursor()  #拿到mysql 游标

sql = 'delete from `%s` where name = `%s`;'
print(sql)
rows= cursor.execute(sql,["user","curry1"])   # 解决 sql 注入
print('%s rows in set'%rows)
conn.commit()   #提交执行的ddl 语句
cursor.close()
conn.close()






