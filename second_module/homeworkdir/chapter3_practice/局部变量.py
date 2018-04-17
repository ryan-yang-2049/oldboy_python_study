#!/usr/bin/env python
#coding:utf-8
'''
局部变量，就是定义在函数里的变量，只能在局部生效。
在函数内部可以引用全局变量。
如果全局和局部都有一个name变量，函数查找变量的顺序是由内而外的。

'''
# name = "ryan"          #全局变量
#
# def change_name():
#     global age
#     age = 22
#     name = 'cherry'   #局部变量
#     print("name",name)
# change_name()
# print(age)