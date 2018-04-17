# -*- coding: utf-8 -*-
"""
__title__ = '05  装饰器复习.py'
__author__ = 'ryan'
__mtime__ = '2018/2/6'
"""

#1 开放封闭原则：对扩展开放，对修改封闭
#2 装饰器本身可以是任意可调用对象，被装饰的对象也可以是任意可调用对象
#3 目的
'''
在遵循：
	1.不修改被装饰对象的源代码
	2.不修改被装饰对象的调用方式
原则下：
	为被装饰对象加上新功能

'''
import time

def timmer(func):
	def inner(*args,**kwargs):
		start = time.time()
		name1 = 'cherry'
		res = func(*args,**kwargs)
		stop = time.time()
		print("运行时间为：%0.1f"%float(stop-start))
		return res
	return inner


@timmer
def index(name):
	time.sleep(1)
	print("welcome %s to linux"%name)
	return 123
	# print(name1)
	# return 123


res = index('ryan')
print(res)







