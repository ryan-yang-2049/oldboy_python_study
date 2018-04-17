# -*- coding: utf-8 -*-
"""
__title__ = '17 yield复习.py'
__author__ = 'yangyang'
__mtime__ = '2018.02.08'
"""

# 例1
# def f1():
# 	print('first')
# 	yield 1
# 	print('second')
# 	yield 2
# 	print('third')
# 	yield 3
#
# g=f1()
# print(g)
#
# print(next(g))
# print(next(g))
# print(next(g))
# try:
# 	print(next(g))
# except StopIteration:
# 	print("not")

# 例子2
# def f1():
# 	while True:
# 		x=yield
# 		print(x)
#
# g=f1()
# # next(g)   # 等同于 g.send(None)
# g.send(None)
# g.send(1)
# g.send(12)
# g.send(123)


# 例3
# import time
# def init(func):
#     def wrapper(*args,**kwargs):
#         g=func(*args,**kwargs)
#         next(g)
#         return g
#     return wrapper
# @init
# def consumer():
#     while True:
#         x=yield
#         print(x)
#
# def producer(target):
#     for i in range(10):
#         time.sleep(1)
#         target.send(i)
#
# producer(consumer())


# 生成器实现生产者消费者
# def init(func):
# 	def wrapper(*args,**kwargs):
# 		g=func(*args,**kwargs)
# 		next(g)
# 		return g
# 	return wrapper
#
# @init
# def consumer(): # 生产者
# 	r = ''
# 	while True:
# 		n = yield r
# 		if not n:
# 			print("not n...")
# 			return
# 		print('3==>[CONSUMER] Consuming %s...' % n)
# 		r = '200 OK'
#
# def produce(c):     # 消费者
# 	n = 0
# 	while n < 2:
# 		n = n + 1
# 		print('1==>[PRODUCER] Producing %s...' % n)
# 		r = c.send(n)
# 		print('2==>[PRODUCER] Consumer return: %s' % r)
# 	c.close()
#
#
# produce(consumer())










