# -*- coding: utf-8 -*-
"""
__title__ = '10 存储过程的执行.py'
__author__ = 'yangyang'
__mtime__ = '2018.03.07'
"""

import  pymysql

conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='homework',charset='utf8')

cursor=conn.cursor()
# 无参执行存储过程
# cursor.callproc('p1')
# print(cursor.fetchall())


# 有参执行存储过程
cursor.callproc('p2',(2,4,0))
cursor.execute('select @_p2_2')
print(cursor.fetchone())

cursor.close()
conn.close()





