#!/usr/bin/env python
#coding:utf-8
# 匿名函数
# 匿名函数作用：1.节省代码量。2.看着更优雅。
res = lambda x,y:x**y #声明一个匿名函数
res2 = lambda  x,y: x*y if x < y else x - y
print(res(2,3))
print(res2(5,3))

data = list(range(1,10))
print(list(map(lambda x:x*x,data)))



