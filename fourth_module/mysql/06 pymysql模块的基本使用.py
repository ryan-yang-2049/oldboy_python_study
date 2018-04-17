# -*- coding: utf-8 -*-
"""
__title__ = '06 pymysql模块的基本使用.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.28'
"""
# import pymysql
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'select * from user where id = 3;'
# rows= cursor.execute(sql)   # 拿到受影响的行数
# print('%s rows in set'%rows)
# cursor.close()
# conn.close()


# py认证过程
# import pymysql
# user = input("用户名：").strip()
# pwd = input("密码：").strip()
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'select * from user where user="%s" and password="%s";'%(user,pwd)
# # sql = 'select * from user where user=\'%s\' and password=\'%s\';'%(user,pwd)
# rows= cursor.execute(sql)   # 拿到受影响的行数
# print('%s rows in set'%rows)
# cursor.close()
# conn.close()
#
# if rows:
# 	print("登陆成功")
# else:
# 	print("登陆失败")



# sql 注入问题
# import pymysql
# user = input("用户名：").strip()
# pwd = input("密码：").strip()
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'select * from user where user="%s" and password="%s";'%(user,pwd)
# # sql = 'select * from user where user=\'%s\' and password=\'%s\';'%(user,pwd)
# print(sql)
# rows= cursor.execute(sql)   # 拿到受影响的行数
# print('%s rows in set'%rows)
# cursor.close()
# conn.close()
#
# if rows:
# 	print("登陆成功")
# else:
# 	print("登陆失败")

'''
#其中的 --  相当于关键字
第一种情况：
用户名：egon" -- hahahaha
密码：
select * from user where user="egon" -- hahahaha" and password="";
1 rows in set
登陆成功

第二种情况：
用户名：xxx" or 1=1 -- hahahaha
密码：
select * from user where user="xxx" or 1=1 -- hahahaha" and password="";
4 rows in set
登陆成功
'''

# 解决sql 注入问题
# import pymysql
# user = input("用户名：").strip()
# pwd = input("密码：").strip()
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'select * from user where user=%s and password=%s;'
# print(sql)
# rows= cursor.execute(sql,[user,pwd])   # 解决 sql 注入
# print('%s rows in set'%rows)
# cursor.close()
# conn.close()
#
# if rows:
# 	print("登陆成功")
# else:
# 	print("登陆失败")


# 增删改
# 都必须要 commit 一次。
#增加
# import pymysql
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'insert into user(user,password) values(%s,%s)'
# rows= cursor.execute(sql,['curry2','123'])   # 解决 sql 注入
# print('%s rows in set'%rows)
# conn.commit()   #提交执行的ddl 语句
# cursor.close()
# conn.close()

# 插入多条
# import pymysql
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'insert into user(user,password) values(%s,%s)'
# rows = cursor.executemany(sql,[('hanxin哈哈','123'),('libai呵呵','123')])
# print('%s rows in set'%rows)
# conn.commit()   #提交执行的ddl 语句
# cursor.close()
# conn.close()

# 查数据
# import pymysql
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
# sql = 'select * from user;'
# rows= cursor.execute(sql)   # 解决 sql 注入
# # 单条查询
# res1 = cursor.fetchone()   # 获得元组 (1, 'egon', '123')
# res2 = cursor.fetchone()
# res3 = cursor.fetchone()
# print(res1,res2,res3)    #(1, 'egon', '123') (2, 'ryan', '1234') (3, 'cherry', '12345')

# 查多条
# print(cursor.fetchmany(3))  # ((1, 'egon', '123'), (2, 'ryan', '1234'), (3, 'cherry', '12345'))
# res2 = cursor.fetchone()    # 4: (4, 'alal', '123') 光标位置
# res3 = cursor.fetchone()
# print("4:",res2)
# print("5:",res3)

# 查所有
# print(cursor.fetchall()) #((1, 'egon', '123'), (2, 'ryan', '1234'),..., (11, 'libai呵呵', '123'))

# 光标的移动
# 绝对位置
# print(cursor.fetchall())        # 数据全部打完
# cursor.scroll(0,mode='absolute') # 光标移动数据的绝对位置，（0 是起始位置）
# print(cursor.fetchone())        # (1, 'egon', '123') 光标此时会移动到第二条数据前面。

# 相对位置
# print(cursor.fetchone())
# print(cursor.fetchone())
# cursor.scroll(1,mode='relative')  #  2 表示光标移动位置，可以是负数
# print(cursor.fetchone())
#
# cursor.close()
# conn.close()



# 查询当前表最后以后一个自增ID号
# import pymysql
#
# conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
# cursor = conn.cursor()  #拿到mysql 游标
#
# sql = 'insert into user(user,password) values(%s,%s);'
# print(sql)
# rows= cursor.execute(sql,['alex','123'])   # 解决 sql 注入
# print('%s rows in set'%rows)
# conn.commit()
# print("最后一个自增ID：",cursor.lastrowid)
# cursor.close()
# conn.close()



import pymysql

conn = pymysql.connect(host='101.132.161.180',user='root',password='123456',database='db1',charset='utf8')
cursor = conn.cursor()  #拿到mysql 游标

sql = 'delete from %s where name = %s ;'
print(sql)
rows= cursor.execute(sql,["user",'curry1'])   # 解决 sql 注入
print('%s rows in set'%rows)
conn.commit()   #提交执行的ddl 语句
cursor.close()
conn.close()














