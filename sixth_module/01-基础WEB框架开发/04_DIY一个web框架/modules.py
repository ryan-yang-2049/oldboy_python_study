# -*- coding: utf-8 -*-

# __title__ = 'modules.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.06.19'


# 生成用户表

import pymysql
#连接数据库
conn = pymysql.connect(host='101.132.161.180',port= 3306,user = 'root',passwd='123456',db='new_web') #db：库名
#创建游标
cur = conn.cursor()

sql='''
create table userinfo(
        id INT PRIMARY KEY ,
        name VARCHAR(32) ,
        password VARCHAR(32)
)

'''

cur.execute(sql)

#提交
conn.commit()
#关闭指针对象
cur.close()
#关闭连接对象
conn.close()



'''
web框架 功能总结
main.py 启动文件 ，封装socket 
1. urls.py ：路径与视图函数映射关系        ---- url 控制器
2. views.py ： 视图函数，固定有一个形参：environ      ---- 视图函数
3. templates文件夹：存放html文件     ---- 模板
4.modules : 在项目启动前，在数据库中创建数据库表结构的       ----与数据相关



'''




