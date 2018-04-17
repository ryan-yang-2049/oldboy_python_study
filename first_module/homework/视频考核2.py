#!/usr/bin/env python
#coding:utf-8


'''
一. 口述题
  开始前请自我介绍（包括为什么来路飞学习Python，和学习后的目标）
  1. 分别解释"=","==","+="的含义
  2. 解释'and','or','not'
  3. "is"和“==”的区别
  4. 数据类型的可变与不可变分别有哪些？
  5.python2和python3的默认字符编码
  6.各个数据类型分别是有序的？还是无序的？

二. 编程题
  1. 求100以内不能被3整除的所有数，并把这些数字放在列表sum=[]里，并求出这些数字的总和和平均数。
  2. 写一个三次认证（编程）


'''


username = "ryan"
password = "1234"

num = 0
while num < 3:
    login_user = input("login:").strip()
    login_passwd = input("password:").strip()
    num += 1
    print(num)
    if login_user == username and login_passwd == password:
        print("登录成功")
        break
    else:
        print("登录失败！")
    if num == 3:
        print("用户被锁!")
        break











