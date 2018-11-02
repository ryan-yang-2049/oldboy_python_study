# -*- coding: utf-8 -*-

# __title__ = '7.装饰器之最后一关.py'
# __author__ = 'YangYang'
# __mtime__ = '2018.09.17'

import functools

def wrapper(func):
	@functools.wraps(func)
	def inner(*args, **kwargs):
		return func(*args, **kwargs)

	return inner

@wrapper
def f1():
	print('f1')

@wrapper
def f2():
	print('f2')

print(f1.__name__)
print(f2.__name__)




