# -*- coding: utf-8 -*-
"""
__title__ = "add_data.py"
__author__ = "yangyang"
__mtime__ = "2018.02.28"
"""
import random

学生表
for i in range(50):
	data = 'insert into student(sname,gender,class_id) values("乔丹%d","女",%d),("艾弗森%d","女",%d),("科比%d","男",%d);'%(i ,random.randint(1,16),i,random.randint(1,16),i,random.randint(1,16))
	print(data)

老师表
insert into teacher(tname) values('张三'),('李四'),('王五');
for i in range(1,11):
	sql = 'insert into teacher(tname) values("张%d"),("李%d");'%(i,i)
	print(sql)

课程表
insert into course(cname,teacher_id) values('生物',1),('体育',1),('物理',2);
for i in range(30):
	sql = 'insert into course(cname,teacher_id) values("生物",%d),("体育",%d),("物理",%d);'%(random.randint(1,21),random.randint(1,21),random.randint(1,21))
	print(sql)

成绩表
for i in range(100):
	sql = "insert into score(student_id,course_id,score) values(%d,%d,%d),(%d,%d,%d);"%(random.randint(1,151),random.randint(1,91),random.randint(30,100),random.randint(1,151),random.randint(1,91),random.randint(30,100))
	print(sql)

任职表
insert into teach2cls(tid,cid) values(1,1),(1,2),(2,1),(3,2);
for i in range(30):
	sql = 'insert into teach2cls(tid,cid) values(%d,%d),(%d,%d),(%d,%d);'%(random.randint(1,20),random.randint(1,15),random.randint(1,20),random.randint(1,15),random.randint(1,20),random.randint(1,15))
	print(sql)







